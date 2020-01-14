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
import zipfile

import pymongo

from scrimmage.utilities import *


class Server:
    def __init__(self):
        # Set up database connection
        self.db_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.db_client["royale"]
        self.db_collection = self.db["teams"]

        self.logs = list()

        self.loop_continue = True

        self.max_simultaneous_runs = 4
        self.max_runs = 20
        self.current_running = [x for x in range(self.max_simultaneous_runs)]
        self.runner_queue = list()
        self.starting_runs = 20

        # Flags
        self.disable_leaderboard = False
        self.disable_visualizer = False

        self.loop = asyncio.get_event_loop()
        self.coro = asyncio.start_server(self.handle_client, IP, PORT, loop=self.loop)
        self.server = self.loop.run_until_complete(self.coro)

        self.loop.run_in_executor(None, self.await_input)
        self.loop.run_in_executor(None, self.runner_loop)
        self.loop.run_in_executor(None, self.visualizer_loop)

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
            elif 'teams' in com:
                [print(x['teamname']) for x in self.db_collection.find()]

            # Write a python command that will get executed
            elif 'exec' in com:
                try:
                    exec(input("WARNING: "))
                except Exception:
                    print('You did it wrong.')

            # Shows the current queue for running clients
            elif 'queue' in com:
                print(*self.runner_queue)

            # Wipes running data for all teams so they will rerun
            elif 'rerun' in com:
                for team in self.db_collection.find():
                    id = team['_id']
                    self.db_collection.update_one({'_id': id}, {'$set': {'average_run': 0}})
                    self.db_collection.update_one({'_id': id}, {'$set': {'best_run': 0}})
                    self.db_collection.update_one({'_id': id}, {'$set': {'temp_total': 0}})
                    self.db_collection.update_one({'_id': id}, {'$set': {'total_runs': 0}})
                    self.db_collection.update_one({'_id': id}, {'$set': {'logs': None}})
                    self.db_collection.update_one({'_id': id}, {'$set': {'error': None}})

            # Leaderboard enabling / disabling
            elif 'enable_leaderboard' in com:
                self.disable_leaderboard = False

            elif 'disable_leaderboard' in com:
                self.disable_leaderboard = True

            # Visualizer enabling / disabling
            elif 'enable_visualizer' in com:
                self.disable_visualizer = False

            elif 'disable_visualizer' in com:
                self.disable_visualizer = True

    async def handle_client(self, reader, writer):
        try:
            command = await reader.read(BUFFER_SIZE)
            command = command.decode()

            cont = 'False'
            if command in REGISTER_COMMANDS + SUBMIT_COMMANDS + VIEW_STATS_COMMANDS + LEADERBOARD_COMMANDS:
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
                elif command in LEADERBOARD_COMMANDS:
                    await self.send_leaderboard(reader, writer)

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
                                       'temp_total': 0,
                                       'total_runs': 0,
                                       'logs': None,
                                       'error': None})

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
        self.db_collection.update_one({'_id': tid}, {'$set': {'code_file': {'name': f'{client["teamname"]}_client.py',
                                                                            'contents': submission}}})
        self.db_collection.update_one({'_id': tid}, {'$inc': {'submissions': 1}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'average_run': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'best_run': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'temp_total': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'total_runs': 0}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'logs': None}})
        self.db_collection.update_one({'_id': tid}, {'$set': {'error': None}})

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
        stats += f'Total Runs: {client["total_runs"]}/{self.max_runs}\n'

        if client['error'] is not None:
            stats += f'\nSubmitted client has an error:\n{client["error"]}\n'

        await asyncio.sleep(0.1)

        # Send info to client
        writer.write(stats.encode())
        await writer.drain()

    async def send_leaderboard(self, reader, writer):
        self.log(f'Attempting leaderboard sending with {writer.get_extra_info("peername")}')

        # Verify client
        entry, cont = await self.verify_client(reader, writer)
        client = entry[0]

        # Inform client of state
        writer.write(cont.encode())
        await writer.drain()
        if cont == 'False':
            return

        # Compile leaderboard
        out_string = ''
        all_teams = [x for x in self.db_collection.find({})]
        sorted_teams = sorted(all_teams, key=lambda s: s['average_run'], reverse=True)
        # Add first 3 entries
        for place, team in zip(range(1, 4), sorted_teams[:min(3, len(all_teams))]):
            out_string += f'{place}: {team["teamname"]} | Average: {team["average_run"]}\n'

        out_string += '...\n'

        # Add personal place to the list
        your_place = sorted_teams.index(client) + 1
        out_string += f'{your_place}/{len(all_teams)}: {client["teamname"]} | Average: {client["average_run"]}\n'

        # Find best run ever
        out_string += '\n'

        best_run = 0
        best_team = ''

        for team in all_teams:
            if team['best_run'] > best_run:
                best_run = team['best_run']
                best_team = team['teamname']

        out_string += f'Best Run: {best_team}, {best_run}\n'

        if self.disable_leaderboard:
            out_string = 'Leaderboard has been disabled at this time.'

        await asyncio.sleep(0.1)

        # Send info to client
        writer.write(out_string.encode())
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
        while self.loop_continue:
            if len(self.runner_queue) == 0 and len(self.current_running) == self.max_simultaneous_runs:
                # Repopulate queue
                for entry in self.db_collection.find({}):
                    if entry['code_file'] is None or entry['total_runs'] >= self.max_runs:
                        continue
                    self.runner_queue.append(entry['_id'])

                continue

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

        entry = [x for x in self.db_collection.find({'_id': client})][0]
        shutil.copy('launcher.pyz', end_path)
        code = entry['code_file']
        binary_to_file(f'{end_path}/{code["name"]}', code['contents'])

        # Copy and run proper file
        f = open(os.devnull, 'w')
        if platform.system() == 'Linux':
            shutil.copy('scrimmage/runner.sh', end_path)
            p = subprocess.Popen('bash runner.sh', stdout=f, cwd=end_path, shell=True)
            stdout, stderr = p.communicate()
        else:
            shutil.copy('scrimmage/runner.bat', end_path)
            p = subprocess.Popen('runner.bat', stdout=f, cwd=end_path, shell=True)
            stdout, stderr = p.communicate()

        results = dict()
        with open(end_path + '/logs/results.json', 'r') as f:
            results = json.load(f)

        score = results['Score']

        entry = [x for x in self.db_collection.find({'_id': client})][0]

        # Update total number of runs
        self.db_collection.update_one({'_id': client}, {'$inc': {'total_runs': 1}})

        # Update best run
        if score > entry['best_run']:
            self.db_collection.update_one({'_id': client}, {'$set': {'best_run': score}})

            # Save log files
            with zipfile.ZipFile(f'{end_path}/logs_temp.zip', 'w') as z:
                for filename in os.listdir(f'{end_path}/logs'):
                    z.write(f'{end_path}/logs/{filename}', arcname=f'logs/{filename}')

            b = file_to_binary(f'{end_path}/logs_temp.zip')
            self.db_collection.update_one({'_id': client}, {'$set': {'logs': {'name': 'logs.zip', 'contents': [b]}}})

        # Update temp total
        self.db_collection.update_one({'_id': client}, {'$inc': {'temp_total': score}})

        entry = [x for x in self.db_collection.find({'_id': client})][0]

        # Update average run amount
        self.db_collection.update_one({'_id': client}, {'$set': {'average_run': entry['temp_total'] / max(1, entry['total_runs'])}})

        if 'Error' in results and results['Error'] is not None:
            self.db_collection.update_one({'_id': client}, {'$set': {'error': results['Error']}})

        shutil.rmtree(end_path)

        self.current_running.append(number)

    def visualizer_loop(self):
        loc = 'scrimmage/vis_temp'
        previous_team = None

        while self.loop_continue:
            # Quick stop loop is visualizer is disabled
            if self.disable_visualizer:
                continue

            all_clients = [x for x in self.db_collection.find({})]
            if len(all_clients) <= 0:
                continue

            client = random.choice(all_clients)

            if client['logs'] is None or client['_id'] == previous_team:
                continue

            self.log(f'Visualizing {client["teamname"]}')
            previous_team = client['_id']

            try:
                if not os.path.exists(loc):
                    os.mkdir(loc)

                # Take logs and copy into directory
                zip_path = f'{loc}/{client["logs"]["name"]}'
                binary_to_file(zip_path, client['logs']['contents'])
                z = zipfile.ZipFile(zip_path, 'r')
                z.extractall(path='scrimmage/vis_temp')

                # Take launcher and copy into the directory
                shutil.copy('launcher.pyz', loc)

                # Take batch file and copy into directory, and run
                f = open(os.devnull, 'w')
                if platform.system() == 'Linux':
                    shutil.copy('scrimmage/vis_runner.sh', loc)
                    p = subprocess.Popen('bash vis_runner.sh', stdout=f, cwd=loc, shell=True)
                    stdout, stderr = p.communicate()
                else:
                    shutil.copy('scrimmage/vis_runner.bat', loc)
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
        self.loop_continue = False

        while True:
            try:
                if os.path.exists('scrimmage/temp'):
                    shutil.rmtree('scrimmage/temp')
                break
            except PermissionError:
                continue
        while True:
            try:
                if os.path.exists('scrimmage/vis_temp'):
                    shutil.rmtree('scrimmage/vis_temp')
                break
            except PermissionError:
                continue

        self.server.close()

        os._exit(0)


if __name__ == '__main__':
    serv = Server()
