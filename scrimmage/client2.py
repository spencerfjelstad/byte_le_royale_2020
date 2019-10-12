import asyncio

from scrimmage.utilities import *


class Client:
    def __init__(self):
        self.reader = None
        self.writer = None

        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.handle_client(self.loop))

    # Determines what action the client wants to do
    async def handle_client(self, loop):
        # Connect
        self.reader, self.writer = await asyncio.open_connection(IP, PORT, loop=loop)
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
            pass
        elif command in SUBMIT_COMMANDS:
            pass
        elif command in VIEW_STATS_COMMANDS:
            pass

    def close(self):
        self.writer.close()
        self.loop.close()
        exit()


if __name__ == '__main__':
    cli = Client()
