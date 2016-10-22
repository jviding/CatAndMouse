import socket, sys

# Use same PORT as for the mouse
f = open('port_number', 'r')
PORT = int(f.readline().strip())
f.close()

# Empty cmsg
open('cmsg','w').close()

# Open socket and listen for cats
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)

print 'Listy: Waiting for incoming connections at port '+str(PORT)+'.'

while 1:
	# Wait for connections
	conn, addr = s.accept()
	while True:
		# Read incoming data
		data = conn.recv(1024)
		if not data:
			break
		else:
			# Append data to cmsg
			with open('cmsg', 'a') as f:
				f.write(data)
				print 'Listy: Received message \''+data.replace('\n','')+'\'.'
			# Execution can be ended
			if 'G' in data:
				sys.exit()
	# Close connection
	conn.close()