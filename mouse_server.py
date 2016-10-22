import sys, socket

HOST = ''
PORT = int(sys.argv[1])

# Open socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

# Wait for cat to connect
while 1:
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		# If no data received, keep waiting
		if not data:
			break
		# MEOW received, end execution
		elif 'MEOW' in data:
			conn.send('OUCH')
			sys.exit() # Killed
	conn.close()