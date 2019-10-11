import socket
import os

from scrimmage.utilities import *


class Client:
    def __init__(self):
        pass

    def start(self):
        print('Welcome to Scrimmage Undertaking Client Communications (SUCC)')
        print('Select an action: register (-r), submit (-s), or view stats(-v).')
        command = input('Enter: ')
        if command not in REGISTER_COMMANDS + SUBMIT_COMMANDS + VIEW_STATS_COMMANDS:
            print('Not a recognized command, closing.')
            exit()

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(2)

        # connect to remote host
        try:
            connection.connect((IP, PORT))
        except TimeoutError:
            print('Could not connect. Try waiting and trying again.')
            exit()

        send_data(connection, command)

        if command in REGISTER_COMMANDS:
            self.register(connection)
        elif command in SUBMIT_COMMANDS:
            self.submit(connection)
        elif command in VIEW_STATS_COMMANDS:
            self.view_stats(connection)

    # Client side team registration
    def register(self, connection):
        # Client provides team name to register if possible
        if os.path.isfile('vi.d'):
            print('You have already registered!')
            connection.close()
            exit()
        teamname = input('Enter team name: ')
        send_data(connection, teamname)

        # Client receives uuid for verification purposes later
        uid = receive_data(connection)
        if uid == 'name already taken':
            print('Team name has already been taken')
        else:
            write_file(uid, 'vID')

    # Client side code submission
    def submit(self, connection):
        # Verify uuid exists
        # Client sends uuid for verification
        # Client verifies file being sent
        # Client sends file
        pass

    # Client side stat viewing
    def view_stats(self, connection):
        # Verify uuid exists
        # Client sends uuid for verification
        # Client receives list of current stats
        pass


if __name__ == '__main__':
    cli = Client()
    cli.start()
