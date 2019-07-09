import socket, select, errno, sys, threading
import time_set as t


HEADER_LENGTH = 10
host = socket.gethostbyname(socket.gethostname())
port = 9090


my_username = input('Username: ')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)


def Send():
    while True:
        message = input(f'{my_username}>')

        if message:
            message = message.encode('utf-8')
            message_header = f'{len(message) :< {HEADER_LENGTH}}'.encode('utf-8')
            client_socket.send(message_header + message)
        try:
            while True:

                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print('connection closed by the server')
                    sys.exit()

                username_length = int(username_header.decode('utf-8').strip())
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                print(f'{username} [{t.time_date[0]}] > {message} ')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error'.format(str(e)))
                sys.exit()
            continue

        except KeyboardInterrupt:
            print('x')


        except Exception as e:
            print('General error'.format(str(e)))
            sys.exit()



Send()