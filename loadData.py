import numpy as np

# Load text and return transition matrix
def getMatrix(filename):
	M = np.zeros((27,27))

	with open(filename) as fn:
		for line in fn:
			words = line.split(" ")
			if words[0] == 'CHAPTER': # Ignore if chapter title
				continue

			prev_i = getIndex(words[0][0]) # First character of text
			words[0] = words[0][1:] # Ignore first character now
		
			for w in words:
				for c in w:
					cur_i = getIndex(c)
					if prev_i == 26 and cur_i == 26: # previous character was also non-alphabetical
						continue
					else:
						#print(prev_i, cur_i)
						M[prev_i][cur_i] += 1
					prev_i = cur_i
	#return M


def getIndex(c):
	ascii = ord(c.lower())
	if ascii >= 97 and ascii <= 122:
		return ascii - 97 # a is index 0
	else:
		return 26 # other character

print(getMatrix('test.txt'))
