import asyncio
import datetime

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

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.server.close()
            self.loop.run_until_complete(self.server.wait_closed())
            self.loop.close()

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
            pass
        elif command in SUBMIT_COMMANDS:
            pass
        elif command in VIEW_STATS_COMMANDS:
            pass

    def log(self, *args):
        for arg in args:
            self.logs.append(f'{datetime.datetime.now()}: {arg}')

    async def close(self, writer):
        await writer.drain()
        writer.close()


if __name__ == '__main__':
    serv = Server()
