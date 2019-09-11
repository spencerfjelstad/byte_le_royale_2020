import socket
import os


class Client:
    def __init__(self):
        self.port = 5007
        self.ip = '134.129.91.220'
        self.buffer_size = 4096

    def start(self):
        print('Welcome to Scrimmage Undertaking Client Connections (SUCC)')
        print('Select an action: register (-r), submit (-s), or view stats(-v).')
        command = input('Enter: ')
        if command not in ['register', '-r', 'submit', '-s', 'view', 'view stats', '-v']:
            print('Not a recognized command, closing.')
            exit()

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(2)

        # connect to remote host
        try:
            connection.connect((self.ip, self.port))
        except TimeoutError:
            print('Could not connect. Try waiting and trying again.')
            exit()

        connection.send(bytes(command, 'utf-8'))

        if command in ['register', '-r']:
            self.register(connection)

    def register(self, connection):
        if os.path.isfile('vi.d'):
            print('You have already registered!')
            connection.close()
            exit()
        teamname = input('Enter team name: ')
        connection.send(bytes(teamname, 'utf-8'))
        uid = connection.recv(self.buffer_size).decode('utf-8')
        self.record_uid(uid)

    def record_uid(self, uid):
	    with open('vi.d', 'a') as f:
	        f.write(uid)

if __name__ == '__main__':
    cli = Client()
    cli.start()
