#!/usr/bin/env python3

import socket

HOST = '0.0.0.0'
PORT = 1337

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(0)
conn, addr = socket.accept()

print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(repr(data))
    conn.sendall(data)