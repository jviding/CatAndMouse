import random

# Lines in a file
def file_len(fname):
	with open(fname) as f:
		for i in enumerate(f, 0):
			pass
		return i

# Returns a random line from a file
def rand_line(fname):
	rand = random.randint(0, file_len(fname)[0])
	with open(fname) as f:
		for i in enumerate(f, 0):
			if i[0] == rand:
				break
		return i