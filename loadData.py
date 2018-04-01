import numpy as np

# Load text and return transition matrix
def getMatrix(filename):
	M = np.zeros((27,27))

	with open(filename) as fn:
		prev_i = -1
		prev_c = None
		for line in fn:
			words = line.split(",")
			if words[0][:7] == 'CHAPTER': # Ignore if chapter title
				continue

			for w in words:
				for c in w:
					cur_i = getIndex(c)

					if cur_i == -1: # if character not letter or space
						continue
					if (prev_i == 26) and (cur_i == 26): # if multiple spaces
						continue

					if prev_i != -1: # if valid previous char
						#print(prev_c, prev_i, c, cur_i)
						M[prev_i][cur_i] += 1
					prev_c = c
					prev_i = cur_i
	return M


def getIndex(c):
	ascii = ord(c.lower())
	if ascii >= 97 and ascii <= 122:
		return ascii - 97 # a is index 0
	elif ascii == 32 or ascii == 10: # space or newline
		return 26 # space
	return -1

# To test
#getMatrix('warpeace.txt')
