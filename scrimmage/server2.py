import asyncio
import datetime
import os

from scrimmage.db import DB
from scrimmage.utilities import *


class Server:
    def __init__(self):
        self.database = DB()

        self.logs = list()

        self.logs = list()

        self.max_simultaneous_runs = 4
        self.current_running = [x for x in range(self.max_simultaneous_runs)]
        self.runner_queue = list()
        self.starting_runs = 20

        self.loop = asyncio.get_event_loop()
        self.coro = asyncio.start_server(self.handle_client, IP, PORT, loop=self.loop)
        self.server = self.loop.run_until_complete(self.coro)

        self.loop.run_in_executor(None, self.await_input)
        # self.loop.run_in_executor(None, self.runner_loop)
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

    async def handle_client(self, reader, writer):
        command = await reader.read(BUFFER_SIZE)
        command = command.decode()

        cont = 'False'
        if command in REGISTER_COMMANDS + SUBMIT_COMMANDS + VIEW_STATS_COMMANDS:
            cont = 'True'
        writer.write(cont.encode())
        if cont == 'False':
            self.log(f'{writer.get_extra_info("peername")} supplied a bad command.')
            await self.close(writer)

        if command in REGISTER_COMMANDS:
            self.register_client(reader, writer)
        elif command in SUBMIT_COMMANDS:
            self.receive_submission(reader, writer)
        elif command in VIEW_STATS_COMMANDS:
            self.send_stats(reader, writer)

    def register_client(self, reader, writer):
        self.log(f'Attempting registration with {writer.get_extra_info("peername")}')
        # Receive teamname
        # Verify veracity of teamname
        # Inform client of state
        # Generate new uuid for client
        # Send uuid to client for verification
        # Register information in database
        pass

    def receive_submission(self, reader, writer):
        self.log(f'Attempting submission with {writer.get_extra_info("peername")}')
        # Receive uuid
        # Verify uuid from database
        # Inform client of state
        # Receive client file
        # Save client file
        # Update database with location of file
        # Increment submissions count
        # Create stats file if need be, wipe existing
        # Set stats location in database if need be
        # Add to the runner queue
        pass

    def send_stats(self, reader, writer):
        self.log(f'Attempting stat sending with {writer.get_extra_info("peername")}')
        # Receive uuid
        # Verify uuid from database
        # Inform client of state
        # Retrieve data from stats file
        # Send info to client
        pass

    def log(self, *args):
        for arg in args:
            self.logs.append(f'{datetime.datetime.now()}: {arg}')

    async def close(self, writer):
        await writer.drain()
        writer.close()


if __name__ == '__main__':
    serv = Server()
