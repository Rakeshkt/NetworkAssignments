#!/usr/bin/python

import socket
HOST ='localhost'
PORT = 1500
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.send(HOST)
data =s.recv(1024)
s.close()
print 'received',repr(data)
print 'macid',repr(d)
