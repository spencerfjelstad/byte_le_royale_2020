import asyncio
import os

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

        # Put uuid into file for verification (vID)
        with open('vID', 'w+') as f:
            f.write(vID)

        print("Registration successful.")
        print("You have been given an ID file. Don't move or lose it!")

    async def submit(self):
        # Check vID for uuid
        # Send uuid
        # Receive state of server
        # Check and verify client file
        # Send client file
        pass

    async def get_stats(self):
        # Check vID for uuid
        # Send uuid
        # Receive state of server
        # Receive stats
        pass


if __name__ == '__main__':
    cli = Client()
