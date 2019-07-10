import socket, select, errno, sys
import time_set as t
from threading import Thread as tr

HEADER_LENGTH = 10
host = socket.gethostbyname(socket.gethostname())
port = 8000


my_username = input('Username: ')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
client_socket.setblocking(1)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

def Recv(self, sock):
    while True:

        username_header = sock.recv(HEADER_LENGTH)
        username_length = int(username_header.decode('utf-8').strip())
        username = sock.recv(username_length).decode('utf-8')

        message_header = sock.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8').strip())
        message = sock.recv(message_length).decode('utf-8')

        print(f'\033{username} [{t.time_date[0]}] > {message} ')
rT = tr(target = Recv, args= ('self', client_socket))
rT.start()

def Snd(self, sock):
    while True:

        message = input(f'{my_username}>')
        message = message.encode('utf-8')
        message_header = f'{len(message) :< {HEADER_LENGTH}}'.encode('utf-8')
        sock.send(message_header + message)



RT = tr(target = Snd, args= ('self', client_socket))
RT.start()

