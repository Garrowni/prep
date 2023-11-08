##########################################################
# Echo Client
# 
# Used with server.py
# handles client side of the echo server.
# uses sockets - https://docs.python.org/3/library/socket.html
##########################################################
import socket

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))