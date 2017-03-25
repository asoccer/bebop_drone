#!/usr/bin/env python

import socket,sys

s = socket.socket()
host = socket.gethostname() #This assigns the 
port = 12397
s.bind(('',port))

s.listen(5)

while True:
	try:
		c,addr = s.accept()
		print "Got connection from", addr
		c.send("received thank you")
		c.close()
	except:
		print "thank you closing"
		sys.exit()
