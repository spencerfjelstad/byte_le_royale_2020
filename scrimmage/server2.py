import asyncio
import datetime
import json
import re
import os
import shutil
from subprocess import Popen
import uuid

from scrimmage.db import DB
from scrimmage.utilities import *


class Server:
    def __init__(self):
        self.database = DB()

        self.logs = list()

        self.max_simultaneous_runs = 4
        self.current_running = [x for x in range(self.max_simultaneous_runs)]
        self.runner_queue = list()
        self.starting_runs = 20

        self.loop = asyncio.get_event_loop()
        self.coro = asyncio.start_server(self.handle_client, IP, PORT, loop=self.loop)
        self.server = self.loop.run_until_complete(self.coro)

        self.loop.run_in_executor(None, self.await_input)
        self.loop.run_in_executor(None, self.runner_loop)
        # self.loop.run_in_executor(None, self.visualizer_loop)

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.server.close()
            self.loop.run_until_complete(self.server.wait_closed())
            self.loop.close()

    def await_input(self):
        print('Server is awaiting admin input.')
        while True:
            com = input('Ɛ>')
            self.log(f'Server command: {com}')
            # Exit command for shutting down the server
            if com == 'exit':
                os._exit(0)

            # Echo back the given string to the user, mostly for testing
            elif 'echo ' in com:
                print(com.replace('echo ', ''))

            # Display all the logs from the current server instance
            elif 'log' in com:
                for s in self.logs:
                    print(s)

            # Create a query of all entries in the database
            elif 'query' in com:
                tid = input('TID: ').strip()
                teamname = input('Team name: ').strip()

                if tid == '':
                    tid = None
                if teamname == '':
                    teamname = None

                print(*[str(e) + '\n' for e in self.database.query(tid, teamname)])

            # Show all entries in the database, equivalent to query with no parameters
            elif 'dump' in com:
                print(*[str(e) + '\n' for e in self.database.dump()])

            # Write a python command that will get executed
            elif 'exec' in com:
                try:
                    exec(input("WARNING: "))
                except Exception:
                    print('You did it wrong.')

            elif 'queue' in com:
                print(*self.runner_queue)

    async def handle_client(self, reader, writer):
        try:
            command = await reader.read(BUFFER_SIZE)
            command = command.decode()

            cont = 'False'
            if command in REGISTER_COMMANDS + SUBMIT_COMMANDS + VIEW_STATS_COMMANDS:
                cont = 'True'
            writer.write(cont.encode())
            if cont == 'False':
                self.log(f'{writer.get_extra_info("peername")} supplied a bad command.')

            else:
                if command in REGISTER_COMMANDS:
                    await self.register_client(reader, writer)
                elif command in SUBMIT_COMMANDS:
                    await self.receive_submission(reader, writer)
                elif command in VIEW_STATS_COMMANDS:
                    await self.send_stats(reader, writer)

            await writer.drain()
            writer.close()
        except ConnectionResetError:
            self.log("Connection has been lost")

    async def register_client(self, reader, writer):
        self.log(f'Attempting registration with {writer.get_extra_info("peername")}')
        # Receive teamname
        teamname = await reader.read(BUFFER_SIZE)
        teamname = teamname.decode()

        # Verify veracity of teamname
        cont = 'True'
        invalid_chars = re.compile(r"[\\/:*?<>|]")
        if invalid_chars.search(teamname):
            cont = 'False'

        if teamname == '' or None:
            cont = 'False'

        if len(self.database.query(teamname=teamname)) > 0:
            cont = 'False'

        # Inform client of state
        writer.write(cont.encode())
        if cont == 'False':
            self.log(f'{writer.get_extra_info("peername")} supplied bad or taken teamname.')
            return

        # Generate new uuid for client
        vID = str(uuid.uuid4())

        # Send uuid to client for verification
        await writer.drain()
        writer.write(vID.encode())

        # Register information in database
        self.database.add_entry(tid=vID, teamname=teamname)

        self.log(f'{writer.get_extra_info("peername")} registered teamname: {teamname} with ID: {vID}')

    async def receive_submission(self, reader, writer):
        self.log(f'Attempting submission with {writer.get_extra_info("peername")}')
        # Receive uuid
        tid = await reader.read(BUFFER_SIZE)
        tid = tid.decode()

        # Verify uuid from database
        cont = 'True'
        entry = self.database.query(tid=tid)
        if len(entry) == 0:
            self.log('Entry not found.')
            cont = 'False'
        elif len(entry) == 1:
            self.log(f'Verified {writer.get_extra_info("peername")}')
        else:
            self.log('Something fucked up somewhere why are there repeat ids')
            cont = 'False'

        if tid in self.runner_queue:
            self.log('Cannot accept new submission, previous still running.')
            cont = 'False'

        # Inform client of state
        writer.write(cont.encode())
        if cont == 'False':
            return

        # Receive client file
        client = entry[0]
        location = f'scrimmage/scrim_clients/{client["teamname"]}/{client["teamname"]}_client.py'
        submission = open(location, 'wb+')
        line = await reader.read(BUFFER_SIZE)
        while line:
            submission.write(line)
            line = await reader.read(BUFFER_SIZE)
        submission.close()

        # Update database with location of file
        self.database.set_code_file(client['tid'], location)

        # Create stats file if need be, wipe existing
        stats_location = f'scrimmage/scrim_clients/{client["teamname"]}/stats.json'
        with open(stats_location, 'w+') as f:
            f.write('')

        # Set stats location in database if need be
        self.database.set_stats_file(client['tid'], stats_location)

        # Add to the runner queue
        for x in range(self.starting_runs):
            self.runner_queue.append(client['tid'])

    async def send_stats(self, reader, writer):
        self.log(f'Attempting stat sending with {writer.get_extra_info("peername")}')
        # Receive uuid
        tid = await reader.read(BUFFER_SIZE)
        tid = tid.decode()

        # Verify uuid from database
        cont = 'True'
        entry = self.database.query(tid=tid)
        if len(entry) == 0:
            self.log('Entry not found.')
            cont = 'False'
        elif len(entry) == 1:
            self.log(f'Verified {writer.get_extra_info("peername")}')
        else:
            self.log('Something fucked up somewhere why are there repeat ids')
            cont = 'False'

        # Inform client of state
        writer.write(cont.encode())
        if cont == 'False':
            return

        # Retrieve data from stats file
        client = entry[0]
        stats = ''
        with open(client['stats_location'], 'r') as f:
            stats += f.read()

        # Send info to client
        await writer.drain()
        writer.write(stats.encode())

    def runner_loop(self):
        while True:
            if len(self.runner_queue) == 0 or len(self.current_running) == 0:
                continue

            client = self.runner_queue.pop()
            num = self.current_running.pop()

            self.loop.run_in_executor(None, self.internal_runner, client, num)

    def internal_runner(self, client, number):
        # Run game
        self.log(f'Running client: {client}')
        if not os.path.exists(f'scrimmage/temp'):
            os.mkdir(f'scrimmage/temp')
        end_path = f'scrimmage/temp/{number}'
        if not os.path.exists(end_path):
            os.mkdir(end_path)

        entry = self.database.query(tid=client)[0]
        shutil.copy('launcher.pyz', end_path)
        shutil.copy(entry['client_location'], end_path)
        shutil.copy('scrimmage/runner.bat', end_path)

        f = open(os.devnull, 'w')
        p = Popen('runner.bat', stdout=f, cwd=end_path, shell=True)
        stdout, stderr = p.communicate()

        woop = {'Score': 0}
        try:
            with open(end_path + '/logs/results.json', 'r') as f:
                woop = json.load(f)
        except json.decoder.JSONDecodeError:
            # File doesn't exist
            pass

        score = woop['Score']

        orig = {'Max Score': 0}
        try:
            with open(entry['stats_location'], 'r') as f:
                orig = json.load(f)
        except json.decoder.JSONDecodeError:
            # File doesn't exist
            pass

        if 'Max Score' in orig:
            if orig['Max Score'] < score:
                orig['Max Score'] = score

        with open(entry['stats_location'], 'r+') as f:
            json.dump(orig, f)

        shutil.rmtree(end_path)

        self.current_running.append(number)

    def log(self, *args):
        for arg in args:
            self.logs.append(f'{datetime.datetime.now()}: {arg}')


if __name__ == '__main__':
    serv = Server()
