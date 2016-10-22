import sys, socket

# Report Listy
def report_listy(node, port, catname, letter):
	try:
		s = socket.socket()
		s.connect(('', port))
		s.send(letter+' '+node.split('.')[0]+' '+catname+'\n')
		s.close
	except:
		print catname+': Notifying Listy failed!'

# Connect mouse
def connect_mouse(node, port, catname, letter):
	try:
		s = socket.socket()
		s.connect((node, port))
		if letter == 'A':
			s.send('MEOW')
			print catname+': MEOW!'
			print 'Mouse: '+s.recv(1024)
			report_listy(node, port, catname, 'G')
		else:
			print catname+': Mouse found!'
			report_listy(node, port, catname, 'F')
	except:
		print sys.argv[2]+': Nothing here.'
	finally:
		s.close()

# START EXECUTION HERE
# (node , port , catname , command)
connect_mouse(sys.argv[3]+'.hpc.cs.helsinki.fi', int(sys.argv[4]), sys.argv[2], sys.argv[1])