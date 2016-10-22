import sys, threading, time
from subprocess import Popen, PIPE
from helper import *

# Cordy
class cordyCat():
	def __init__(self, port):
		self.mem = []
		self.port = port
		self.attack = False
		self.lock = threading.Lock()
	# Check if mouse has been found
	def mouse_found(self):
		with open('cmsg') as f:
			for line in f:
				return True
		return False
	# For Catty and Jazzy to get their next command
	def next_move(self, cat):
		if self.mouse_found(): # If mouse has been found, attack
			return self.attack_move(cat)
		else: # If mouse hasn't been found, keep looking
			return self.random_move(cat)
	# Try to find the mouse from a random location
	def random_move(self, cat):
		next = rand_line('ukkonodes')
		while next in self.mem: # Get a node we haven't searched yet
			next = rand_line('ukkonodes')
		self.mem.append(next)
		return 'S '+cat+' '+next[1].split('.')[0]+' '+str(self.port)
	# Attack command
	def attack_move(self, cat):
		this = False
		other = False
		with open('cmsg') as f:
			for line in f:
				if cat in line:
					this = True
				else:
					other = True
				if 'G' in line:
					sys.exit()
		return self.attack_command(cat, this, other, line.split(' ')[1])
	# Give the command in right form
	def attack_command(self, cat, this, other, target):
		if this == True and other == True:
			with self.lock: # Atomic
				if self.attack == False:
					self.attack = True
					return 'A '+cat+' '+target+' '+str(port)
				else:
					return None
		elif this == True and other == False:
			return None
		elif this == False and other == True:
			return 'S '+cat+' '+target+' '+str(port)

# Catty and Jazzy
class catThread (threading.Thread):
	def __init__(self, cordy, name):
		threading.Thread.__init__(self)
		self.cordy = cordy
		self.name = name
	def run(self):
		while 1:
			# Get next command from Cordy
			cmd = ['python','chase_cat.py']
			move = self.cordy.next_move(self.name)
			if move != None:
				print move.split(' ')[1]+': '+move.split(' ')[0]+' '+move.split(' ')[2]
				time.sleep(12)
				cmd.extend(move.split(' '))
				process = Popen(cmd, stdout=PIPE, stderr=PIPE)
				stdout, stderr = process.communicate()
				print stdout.strip()


# Port where to look for the mouse
f = open('port_number', 'r')
port = int(f.readline().strip())
f.close()

# Init Cordy
cordy = cordyCat(port)
# Create Threads for Catty and Jazzy
catty = catThread(cordy, 'Catty')
jazzy = catThread(cordy, 'Jazzy')
# Run the Threads
catty.start()
jazzy.start()