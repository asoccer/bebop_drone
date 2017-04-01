import socket,sys

def send_message(MESSAGE):

	PORT = 5005
	BUFFER= 1024 #Lower for faster response
	s = socket.socket()
	host = '192.168.50.133'
	port = 12397 
	s.connect((host,port))
	s.send(MESSAGE)
	data = s.recv(1024)
	return data
	s.close()

while True:
	msg = raw_input("Send to Drone\n")
	if(msg == "stop"):
		response = send_message(msg)
		sys.exit()
		break
#	print msg
	response = send_message(msg)
	print response
