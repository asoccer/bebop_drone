import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
options = {1: 'EOff',2:'Toff',3:'Land',4:'Lroll',6:'RRoll'}
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >> sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            choice = int(data)
            if choice not in options.keys():
                print >> sys.stderr, 'not recognized command'
                connection.sendall('wrong command')
            else:
                print >> sys.stderr, 'Command Received->' + options.get(choice)
                connection.sendall(options.get(choice))
            
    finally:
        # Clean up the connection
        connection.close()