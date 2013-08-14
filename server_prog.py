#!/usr/bin/python 
import socket
import uuid
HOST = 'localhost'
PORT = 1500
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'connected by', addr
print uuid.getnode()
d = uuid.getnode()
while True:
     data = conn.recv(1024)
     if not data: break
     conn.send(d)
     conn.send(data)
conn.close()
