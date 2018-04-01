import random

import loadData

def encrypt(filename):
	random.seed(1234) # So its the same every time

	in_string = ""

	# Re-format original text
	with open(filename) as fn:
		prev_i = -1
		prev_c = None

		for line in fn:
			words = line.split(",")
			for w in words:
				for c in w:
					cur_i = loadData.getIndex(c)

					if cur_i == -1: # if character not letter or space
						continue
					if (prev_i == 26) and (cur_i == 26): # if multiple spaces
						continue
					if prev_c == None:
						in_string += c.lower()

					if prev_i != -1: # if valid previous char
						#print(prev_c, prev_i, c, cur_i)
						in_string += c.lower()
					prev_c = c
					prev_i = cur_i

	# Perform encryption
	mapping = [i for i in range(27)]
	random.shuffle(mapping)
	encrypted_string = ''

	# Encrypt each character
	for i in range(len(in_string)):
		encrypted_string += encryptChar(in_string[i], mapping)
	return encrypted_string

def encryptChar(c, mapping):
	i = loadData.getIndex(c)
	if i != -1:
		new_i = mapping[i]
		if new_i == 26:
			return ' '
		else:
			return chr(new_i + 97)


# To test
#print(encrypt('prideprejudice.txt'))