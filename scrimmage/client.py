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
        if command not in ['register', '-r', 'submit', '-s', 'view', 'view stats', '-v']:
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

        if command in ['register', '-r']:
            self.register(connection)

    # Client side team registration
    def register(self, connection):
        if os.path.isfile('vi.d'):
            print('You have already registered!')
            connection.close()
            exit()
        teamname = input('Enter team name: ')
        send_data(connection, teamname)

        uid = receive_data(connection)
        if uid == 'name already taken':
            print('Team name has already been taken')
        else:
            write_file(uid, 'vID')


if __name__ == '__main__':
    cli = Client()
    cli.start()
