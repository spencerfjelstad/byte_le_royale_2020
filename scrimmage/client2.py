import asyncio
import os

from game.config import CLIENT_DIRECTORY, CLIENT_KEYWORD
from scrimmage.utilities import *


class Client:
    def __init__(self):
        self.reader = None
        self.writer = None

        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.handle_client())

    # Determines what action the client wants to do
    async def handle_client(self):
        # Connect
        self.reader, self.writer = await asyncio.open_connection(IP, PORT, loop=self.loop)
        print('Connected successfully.')

        print('Select an action: register (-r), submit (-s), or view stats(-v).')
        command = input('Enter: ')

        if command not in REGISTER_COMMANDS + SUBMIT_COMMANDS + VIEW_STATS_COMMANDS:
            print('Not a recognized command.')
            return

        self.writer.write(command.encode())
        cont = await self.reader.read(BUFFER_SIZE)
        cont = cont.decode()
        if cont == 'False':
            print('Server caught an illegal command.')
            return

        if command in REGISTER_COMMANDS:
            await self.register()
        elif command in SUBMIT_COMMANDS:
            await self.submit()
        elif command in VIEW_STATS_COMMANDS:
            await self.get_stats()

    async def register(self):
        # Check if vID already exists and cancel out
        if os.path.isfile('vID'):
            print('You have already registered.')
            return

        # Ask for teamname
        teamname = input("Enter your teamname: ")

        # Send teamname
        self.writer.write(teamname.encode())

        # Receive state of server
        cont = await self.reader.read(BUFFER_SIZE)
        cont = cont.decode()
        if cont == 'False':
            print('Teamname contains illegal characters or is already taken.')
            return

        # Receive uuid
        vID = await self.reader.read(BUFFER_SIZE)
        vID = vID.decode()

        if vID == '':
            print('Something broke.')
            return

        # Put uuid into file for verification (vID)
        with open('vID', 'w+') as f:
            f.write(vID)

        print("Registration successful.")
        print("You have been given an ID file. Don't move or lose it!")
        print("You can give a copy to your teammates so they can submit and view stats.")

    async def submit(self):
        # Check vID for uuid
        if not os.path.isfile('vID'):
            print("Cannot find vID, please register first.")

        tid = ''
        with open('vID', 'r') as f:
            tid = f.read()

        # Send uuid
        self.writer.write(tid.encode())

        # Receive state of server
        cont = await self.reader.read(BUFFER_SIZE)
        cont = cont.decode()

        if cont == 'False':
            print('Cannot submit at this time.')

        # Check and verify client file
        file = None
        for filename in os.listdir(CLIENT_DIRECTORY):
            if CLIENT_KEYWORD.upper() not in filename.upper():
                # Filters out files that do not contain CLIENT_KEYWORD in their filename
                continue

            if os.path.isdir(os.path.join(CLIENT_DIRECTORY, filename)):
                # Skips folders
                continue

            user_check = input(f'Submitting {filename}, is this ok? (y/n): ')
            if 'y' in user_check.lower():
                file = filename
                break
        else:
            file = input('Could not find file: please manually type file name: ')

        if not os.path.isfile(file):
            print('File not found.')
            return

        # Send client file
        print('Submitting file.')
        f = open(file, 'rb')
        line = f.read(BUFFER_SIZE)
        while line:
            self.writer.write(line)
            line = f.read(BUFFER_SIZE)
            await self.writer.drain()

        print('File sent successfully.')

    async def get_stats(self):
        # Check vID for uuid
        if not os.path.isfile('vID'):
            print("Cannot find vID, please register first.")

        tid = ''
        with open('vID', 'r') as f:
            tid = f.read()

        # Send uuid
        self.writer.write(tid.encode())

        # Receive state of server
        cont = await self.reader.read(BUFFER_SIZE)
        cont = cont.decode()

        if cont == 'False':
            print('Failure in sending ID.')

        # Receive stats
        stats = await self.reader.read(BUFFER_SIZE)
        stats = stats.decode()
        print(stats)


if __name__ == '__main__':
    cli = Client()