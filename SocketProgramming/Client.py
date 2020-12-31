import socket
from time import sleep

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True :

        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print('Received', repr(data))
        sleep(1)


