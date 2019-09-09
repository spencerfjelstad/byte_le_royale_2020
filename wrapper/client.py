import socket


class Client:
    def __init__(self):
        self.port = 5007
        self.ip = '134.129.91.220'

    def start(self):
        print('Welcome to Scrimmage Undertaking Client Connections (SUCC)')
        print('Select an action: register (-r), submit (-s), or view stats(-v).')
        command = input('Enter: ')
        if command not in ['register', '-r', 'submit', '-s', 'view', 'view stats', '-v']:
            print('Not a recognized command, closing.')
            exit()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        # connect to remote host
        try:
            s.connect((self.ip, self.port))
        except TimeoutError:
            print('Could not connect. Try waiting and trying again.')
            exit()

        s.send(bytes(command, 'utf-8'))


if __name__ == '__main__':
    cli = Client()
    cli.start()
