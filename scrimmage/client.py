import socket
import os

from game.config import CLIENT_DIRECTORY, CLIENT_KEYWORD
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

        connection.close()

    # Client side team registration
    def register(self, connection):
        # Client provides team name to register if possible
        if os.path.isfile('vID'):
            print('You have already registered!')
            return
        teamname = input('Enter team name: ')
        send_data(connection, teamname)

        # Client receives uuid for verification purposes later
        uid = receive_data(connection)
        if uid == 'name already taken':
            print('Team name has already been taken')
            return

        write_file(uid, 'vID')
        print('Registration successful.')

    # Client side vID verification
    def verify(self, connection):
        # Verify file exists
        if not os.path.isfile('vID'):
            return False

        # Grab vid from file
        vid = None
        with open('vID', 'r') as f:
            vid = f.read()

        # Verify things were in the file
        if vid is not None or vid is '':
            return False

        # Send vid over
        send_data(connection, vid)
        return True

    # Client side code submission
    def submit(self, connection):
        # Verify uuid exists
        if not self.verify(connection):
            print('Could not verify client.')
            return

        state = receive_data(connection)
        if state == 'does not exist':
            print('Could not find registered user.')
            return

        # Client verifies file being sent
        file = None
        for filename in os.listdir(CLIENT_DIRECTORY):
            filename = filename.replace('.py', '')

            if CLIENT_KEYWORD.upper() not in filename.upper():
                # Filters out files that do not contain CLIENT_KEYWORD in their filename
                continue

            if os.path.isdir(os.path.join(CLIENT_DIRECTORY, filename)):
                # Skips folders
                continue

            user_check = input(f'Submitting {filename}, is this ok? (y/n): ')
            if 'y' in user_check.lower():
                file = filename
        else:
            file = input('Could not find file: please manually type file name: ')

        if not os.path.isfile(file):
            print('File not found.')
            return

        # Client sends file
        f = open(file, 'rb')
        line = f.read(BUFFER_SIZE)
        while line:
            connection.send(line)
            line = f.read(BUFFER_SIZE)
        f.close()

    # Client side stat viewing
    def view_stats(self, connection):
        # Verify uuid exists
        if not self.verify(connection):
            print('Could not verify client.')
            return

        # Client receives list of current stats
        pass


if __name__ == '__main__':
    cli = Client()
    cli.start()
