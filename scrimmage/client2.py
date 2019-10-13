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
            print('Not a recognized command, closing.')
            self.close()

        self.writer.write(command.encode())
        cont = await self.reader.read(BUFFER_SIZE)
        cont = cont.decode()
        if cont == 'False':
            print('1: Server shut down connection.')
            self.close()

        if command in REGISTER_COMMANDS:
            self.register()
        elif command in SUBMIT_COMMANDS:
            self.submit()
        elif command in VIEW_STATS_COMMANDS:
            self.get_stats()

    def register(self):
        # Ask for teamname
        # Send teamname
        # Receive state of server
        # Receive uuid
        # Put uuid into file for verification (vID)
        pass

    def submit(self):
        # Check vID for uuid
        # Send uuid
        # Receive state of server
        # Check and verify client file
        # Send client file
        pass

    def get_stats(self):
        # Check vID for uuid
        # Send uuid
        # Receive state of server
        # Receive stats
        pass

    def close(self):
        os._exit(0)


if __name__ == '__main__':
    cli = Client()
