import asyncio
import datetime
import json
import random
import re
import os
import shutil
import subprocess
import platform
import uuid

import pymongo

from scrimmage.utilities import *


class Server:
    def __init__(self):
        # Set up database connection
        self.db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.db_client["royale"]
        self.db_collection = self.db["teams"]

        self.logs = list()

        self.max_simultaneous_runs = 4
        self.current_running = [x for x in range(self.max_simultaneous_runs)]
        self.runner_queue = list()
        self.starting_runs = 20

        self.loop = asyncio.get_event_loop()
        self.coro = asyncio.start_server(self.handle_client, IP, PORT, loop=self.loop)
        self.server = self.loop.run_until_complete(self.coro)

        self.loop.run_in_executor(None, self.await_input)
        #self.loop.run_in_executor(None, self.runner_loop)
        #self.loop.run_in_executor(None, self.visualizer_loop)

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.close_server()

    def await_input(self):
        print('Server is awaiting admin input.')
        while True:
            com = input('Ɛ>')
            self.log(f'Server command: {com}')
            # Exit command for shutting down the server
            if com == 'exit':
                self.close_server()

            # Echo back the given string to the user, mostly for testing
            elif 'echo ' in com:
                print(com.replace('echo ', ''))

            # Display all the logs from the current server instance
            elif 'log' in com:
                for s in self.logs:
                    print(s)

            # Create a query of all entries in the database
            elif 'query' in com:
                teamname = input('Team name: ').strip()

                if teamname == '':
                    teamname = None

                [print(x) for x in self.db_collection.find({"teamname": teamname})]

            # Show all entries in the database, equivalent to query with no parameters
            elif 'dump' in com:
                [print(x) for x in self.db_collection.find()]

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
            await writer.drain()
            if cont == 'False':
                self.log(f'{writer.get_extra_info("peername")} supplied a bad command.')

            else:
                if command in REGISTER_COMMANDS:
                    await self.register_client(reader, writer)
                elif command in SUBMIT_COMMANDS:
                    await self.receive_submission(reader, writer)
                elif command in VIEW_STATS_COMMANDS:
                    await self.send_stats(reader, writer)

            writer.close()
            await writer.wait_closed()
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
            self.log(f'{writer.get_extra_info("peername")} supplied name with illegal characters.')
            cont = 'False'

        if teamname == '' or None:
            self.log(f'{writer.get_extra_info("peername")} supplied empty name.')
            cont = 'False'

        if len([x for x in self.db_collection.find({"teamname": teamname})]) > 0:
            self.log(f'{writer.get_extra_info("peername")} supplied taken team name.')
            cont = 'False'

        # Inform client of state
        writer.write(cont.encode())
        await writer.drain()

        if cont == 'False':
            return

        # Generate new uuid for client
        vID = str(uuid.uuid4())

        await asyncio.sleep(0.5)

        # Send uuid to client for verification
        writer.write(vID.encode())
        await writer.drain()

        # Register information in database
        self.db_collection.insert_one({'_id': vID,
                                       'teamname': teamname,
                                       'code_file': None,
                                       'submissions': 0,
                                       'average_run': 0,
                                       'best_run': 0,
                                       'temp_total': 0})

        self.log(f'{writer.get_extra_info("peername")} registered teamname: {teamname} with ID: {vID}')

    async def receive_submission(self, reader, writer):
        self.log(f'Attempting submission with {writer.get_extra_info("peername")}')

        # Verify client
        entry, cont = await self.verify_client(reader, writer)

        # Inform client of state
        writer.write(cont.encode())
        await writer.drain()
        if cont == 'False':
            return

        # Receive client file
        client = entry[0]
        tid = client['_id']

        submission = list()
        line = await reader.read(BUFFER_SIZE)
        while line:
            submission.append(line)
            line = await reader.read(BUFFER_SIZE)

        # Update database with submission and stats
        self.db_collection.update_one({'_id': tid}, {'$set': {'code file': {'name': f'{client["teamname"]}_client.py',
                                                                            'contents': submission}}})
        self.db_collection.update_one({'_id': tid}, {'$inc': {'submissions': 1}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'average_run': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'best_run': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'temp_total': 0}})

        # Add to the runner queue
        for x in range(self.starting_runs):
            self.runner_queue.append(tid)

    async def send_stats(self, reader, writer):
        self.log(f'Attempting stat sending with {writer.get_extra_info("peername")}')

        # Verify client
        entry, cont = await self.verify_client(reader, writer)

        # Inform client of state
        writer.write(cont.encode())
        await writer.drain()
        if cont == 'False':
            return

        # Retrieve data from stats file
        client = entry[0]
        stats = ''
        stats += f'Submission: {client["submissions"]}\n'
        stats += f'Average Run: {client["average_run"]}\n'
        stats += f'Best Run: {client["best_run"]}\n'

        await asyncio.sleep(0.1)

        # Send info to client
        writer.write(stats.encode())
        await writer.drain()

    async def verify_client(self, reader, writer):
        # Receive uuid
        tid = await reader.read(BUFFER_SIZE)
        tid = tid.decode()

        # Verify uuid from database
        cont = 'True'
        entry = [x for x in self.db_collection.find({'_id': tid})]
        if len(entry) == 0:
            self.log('Entry not found.')
            cont = 'False'
        elif len(entry) == 1:
            self.log(f'Verified {writer.get_extra_info("peername")}')
        else:
            self.log('Something fucked up somewhere why are there repeat ids')
            cont = 'False'

        return entry, cont

    def runner_loop(self):
        while True:
            if len(self.runner_queue) == 0 or len(self.current_running) == 0:
                continue

            client = self.runner_queue.pop()
            num = self.current_running.pop()

            try:
                self.loop.run_in_executor(None, self.internal_runner, client, num)
            except PermissionError:
                continue

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

        # Copy and run proper file
        if platform.system() == 'Linux':
            shutil.copy('scrimmage/runner.sh')
            subprocess.call(['bash', f'{end_path}/runner.sh'])
        else:
            shutil.copy('scrimmage/runner.bat', end_path)
            f = open(os.devnull, 'w')
            p = subprocess.Popen('runner.bat', stdout=f, cwd=end_path, shell=True)
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

                # Add logs to location
                client_log_location = self.database.change_logs(entry, end_path)

                # Add logs location to database
                self.database.set_logs_location(entry['tid'], client_log_location)

        with open(entry['stats_location'], 'r+') as f:
            json.dump(orig, f)

        shutil.rmtree(end_path)

        self.current_running.append(number)

    def visualizer_loop(self):
        if not os.path.exists(f'scrimmage/vis_temp'):
            os.mkdir(f'scrimmage/vis_temp')

        while True:
            all_clients = self.database.dump()
            if len(all_clients) <= 0:
                continue

            client = random.choice(all_clients)

            if client['logs_location'] is None or client['tid'] in self.runner_queue:
                continue

            self.log(f'Visualizing {client["teamname"]}')

            try:
                # Create custom running directory
                self.database.await_lock()
                loc = 'scrimmage/vis_temp'

                # Take logs and copy into directory
                shutil.copytree(client['logs_location'], f'{loc}/logs')
                self.database.lock = False

                # Take launcher and copy into the directory
                shutil.copy('launcher.pyz', loc)

                # Take batch file and copy into directory, and run
                if platform.system() == 'Linux':
                    shutil.copy('scrimmage/vis_runner.sh', loc)
                    subprocess.call(['bash', f'{loc}/vis_runner.sh'])
                else:
                    shutil.copy('scrimmage/vis_runner.bat', loc)
                    f = open(os.devnull, 'w')
                    p = subprocess.Popen('vis_runner.bat', stdout=f, cwd=loc, shell=True)
                    stdout, stderr = p.communicate()

                # Clean up the directory
                shutil.rmtree(loc)

            except PermissionError:
                continue

    def log(self, *args):
        for arg in args:
            self.logs.append(f'{datetime.datetime.now()}: {arg}')

    def close_server(self):
        if os.path.exists('scrimmage/temp'):
            shutil.rmtree('scrimmage/temp')
        if os.path.exists('scrimmage/vis_temp'):
            shutil.rmtree('scrimmage/vis_temp')

        self.server.close()

        os._exit(0)


if __name__ == '__main__':
    serv = Server()
