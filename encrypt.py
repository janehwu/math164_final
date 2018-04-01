import loadData

def encrypt(filename):
	encrypted_string = ""

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
						encrypted_string += c.lower()

					if prev_i != -1: # if valid previous char
						#print(prev_c, prev_i, c, cur_i)
						encrypted_string += c.lower()
					prev_c = c
					prev_i = cur_i
	return encrypted_string

# To test
#print(encrypt('prideprejudice.txt'))