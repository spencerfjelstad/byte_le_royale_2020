import os
import socket
from thread import Thread


class Server:
    def __init__(self):
        self.port = 5007
        self.ip = '134.129.91.220'
        self.buffer_size = 4096

        self.connections = list()

        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(10)
        print('Server started and listening.')

        server_input = Thread(self.await_input, ())
        server_input.start()

        while True:
            connection, address = self.server_socket.accept()
            print(f'Connection from {address}.')

            client_thread = Thread(self.handle_client, (connection, address,))
            client_thread.start()

    def handle_client(self, connection, address):
        command = connection.recv(self.buffer_size).decode('utf-8')
        print(command)
        connection.close()

    def await_input(self):
        print('Server is awaiting admin input.')
        while True:
            com = input()
            if com == 'exit':
                os._exit(0)
            elif 'echo ' in com:
                print(com.replace('echo ', ''))


if __name__ == '__main__':
    serv = Server()
    serv.start()
