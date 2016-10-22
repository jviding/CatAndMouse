import paramiko, random, getpass
from helper import *

# Open SSH session in Node
def open_SSH(node):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(node, username=getpass.getuser(), password=None, key_filename='/home/'+getpass.getuser()+'/.ssh/id_rsa.pub')
	return ssh

# Copy mouse_server.py to node server
def scp_mouse(ssh):
	sftp = ssh.open_sftp()
	sftp.put('mouse_server.py', 'mouse_server.py')
	sftp.close()

# Start executing mouse in socket
def waitInHide(ssh, port):
	stdin, stdout, stderr = ssh.exec_command('python mouse_server.py '+str(port))
	wait = stdout.readlines()
	wait = stderr.readlines() # Blocks until mouse_server.py ends
	stdin, stdout, stderr = ssh.exec_command('rm mouse_server.py')
	ssh.close()
	print 'Mouse: Caught.'

# Start mouse.py in a Node
def deploy_mouse(port):
	node = rand_line('ukkonodes')[1].strip() # Random Node from ukkonodes
	ssh = open_SSH(node) # SSH to node using public key
	scp_mouse(ssh) # Deploy mouse to randomly chosen Node
	print 'Mouse: Hiding at '+node.split('.')[0]+'.'
	waitInHide(ssh, port)

# Port for mouse
f = open('port_number', 'r')
port = int(f.readline().strip())
f.close()

# Deploy mouse in to a random Node
deploy_mouse(port)