#!/usr/bin/env python3

import socket

HOST = '192.168.100.9'
PORT = 1337

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
socket.sendall(b'Hello cat!')

data = socket.recv(1024)

print('Received: ' + repr(data))