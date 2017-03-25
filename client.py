import socket

def send_message(MESSAGE):

	PORT = 5005
	BUFFER= 1024 #Lower for faster response
	s = socket.socket()
	host = '192.168.50.133'
	port = 12397 
	s.connect((host,port))
	s.send(MESSAGE)
	data = s.recv(1024)
	print data
	s.close()

send_message("ayylmao")
