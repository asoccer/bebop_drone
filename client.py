import socket
TCP_IP = '192.168.50.133'
PORT = 5005
BUFFER= 1024
MESSAGE = "hello world"

s = socket.socket()
host = TCP_IP
port = 12397

s.connect((host,port))
print s.recv(1024)
s.close()
