import os
import socket
import datetime
import uuid
from thread import Thread


class Server:
    def __init__(self):
        self.port = 5007
        self.ip = '127.0.0.1'
        self.buffer_size = 4096

        self.connections = list()

        self.server_socket = None

        self.logs = list()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(10)
        print('Server started and listening.')

        server_input = Thread(self.await_input, ())
        server_input.start()

        while True:
            connection, address = self.server_socket.accept()
            self.log(f'Connection from {address}.')

            client_thread = Thread(self.handle_client, (connection, address,))
            client_thread.start()

    def handle_client(self, connection, address):
        command = connection.recv(self.buffer_size).decode('utf-8')
        if command in ['register', '-r']:
            self.register_client(connection, address)
        connection.close()

    def register_client(self, connection, address):
        teamname = connection.recv(self.buffer_size).decode('utf-8')
        team_uuid = self.generate_uid()
        self.record_uid(teamname, team_uuid)
        self.log(f'Registering team {teamname} with {team_uuid}')
        connection.send(bytes(team_uuid,'utf-8'))



    def await_input(self):
        print('Server is awaiting admin input.')
        while True:
            com = input()
            self.log(f'Server command: {com}')
            if com == 'exit':
                os._exit(0)
            elif 'echo ' in com:
                print(com.replace('echo ', ''))
            elif 'log' in com:
                for s in self.logs:
                    print(s)

    def generate_uid(self):
	    id = str(uuid.uuid4())
	    return id

    def record_uid(self, team, uid):
	    with open('s_vi.d', 'a') as f:
	        f.write(team + ' ' + uid + '\n')
	
    def log(self, *args):
        for arg in args:
            self.logs.append(f'{datetime.datetime.now()}: {arg}')


if __name__ == '__main__':
    serv = Server()
    serv.start()
