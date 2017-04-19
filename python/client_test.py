from msvcrt import getch

print 'Welcoem to Bebop controller'
print 'Attempting to connect to server...'

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#Replace localhsot w/ Drone IP

server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

print 'Connection to Server established.'
options = {1: 'EOff',2:'Toff',3:'Land',4:'Lroll',5:'RRoll'}
options_keys = options.keys()
while True: 
	menu = '1 - Emergency Power off Mode\n2 - Take oFf/hover\n3 - Land\n4 - Left Roll\n6 - Right Roll\n'
	print menu
	select = getch()
	sock.sendall(select)
	if select=='9':
		sock.close()
		sys.exit(1)
	amount_expected = len(select)
	amount_received = 0;
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
	print 'The Server Sent the follwoing->\t' + data + '\n\n\n'
        









