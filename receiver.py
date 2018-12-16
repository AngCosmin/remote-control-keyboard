#!/usr/bin/env python3
import json
import socket
from time import sleep

from pynput.keyboard import Key, Listener, Controller, KeyCode

keyboard = Controller()
# sleep(1)
# keyboard.press(Key.__getattr__('backspace'))
# sleep(1)
# keyboard.release(Key(KeyCode(91)))
# sleep(1)
# keyboard.press(Key.esc)
# sleep(1)
# keyboard.release(Key.esc)

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

    event = json.loads(data)

    if event['type'] == 'press':
        if len(event['key']) == 1:
            keyboard.press(event['key'])
        else:
            keyboard.press(Key.__getattr__(event['key']))
    elif event['type'] == 'release':
        if len(event['key']) == 1:
            keyboard.release(event['key'])
        else:
            keyboard.release(Key.__getattr__(event['key']))
