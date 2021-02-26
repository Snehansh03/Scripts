#!/usr/bin/env python

import socket

HOST = '10.0.2.13'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)

print('Received', repr(data))