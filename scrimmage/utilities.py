import threading

#IP = '134.129.91.220'
IP = '127.0.0.1'
PORT = 5007
BUFFER_SIZE = 4096

REGISTER_COMMANDS = ['register', '-r']
SUBMIT_COMMANDS = ['submit', '-s']
VIEW_STATS_COMMANDS = ['view stats', 'view', '-v']


class Thread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func

    def run(self):
        self.func(*self.args)


def write_file(data, name):
    with open(name, "w+") as f:
        f.write(data)


def send_data(connection, data):
    connection.send(bytes(data, 'utf-8'))


def receive_data(connection):
    return connection.recv(BUFFER_SIZE).decode('utf-8')
