#!/usr/bin/env python

import socket,sys



s = socket.socket()
host = socket.gethostname()
port = 12397

s.bind(('',port))

s.listen(5)

while True:
	try:
		c,addr = s.accept()
		data = c.recv(1024)
		print "Got connection from", addr
		print "data received ->", data

		c.send("received thank you")
		c.close()
		if(data == "stop"):
			sys.exit()	
		
	except:
		print "thank you closing"
		sys.exit()
