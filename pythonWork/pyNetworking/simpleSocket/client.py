##########################################################
# client.py for simple socket
# 
# Used with server.py
# handles client side of the server.
# uses sockets - https://docs.python.org/3/library/socket.html
##########################################################
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))