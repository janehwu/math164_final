import loadData
import math
import random
import numpy

def score(M, phrase):
    """Score for one phrase"""
    total = 0
    for i in range(1, len(phrase)):
        # Get index from probability matrix
        previous = ord(phrase[i-1].lower()) - 97
        current = ord(phrase[i].lower()) - 97
        if previous == -65: #space
            previous = 26
        if current == -65: #space
            current = 26
        
        # Total score
        total += math.log(1 + M[previous][current])
    return total

def decrypt(perm, phrase):
    """Decypt the current text using the current permutation"""
    text = ""
    for i in range(len(phrase)):
        index = 26
        if phrase[i] != ' ':
            index = ord(phrase[i]) - 97
        text = text + perm[index]
    return text

def MCMC(numIterations, inputText, sampleFile = "warpeace.txt"):
    probM = getMatrix(sampleFile)

    # The default permutation
    perm = [chr(i) for i in range(97, 123)] + [' ']
    scoreDict = {}
    currScore = score(probM, inputText)
    scoreDict[tuple(perm)] = currScore

    for i in range(numIterations):
        # Swap two different letters in the permutation
        # (a transition in the Markov chain)
        rand1 = random.randint(0, 26)
        rand2 = random.randint(0, 26)
        while rand1 == rand2:
            rand2 = random.randint(0, 26)
        testperm = perm[:]
        testperm[rand1] = perm[rand2]
        testperm[rand2] = perm[rand1]

        # Score this new encryption
        if tuple(testperm) not in scoreDict.keys():
            scoreDict[tuple(testperm)] = score(probM, decrypt(testperm, inputText))
        testscore = scoreDict[tuple(testperm)]
        
        acceptValue = math.exp(scoreDict[tuple(testperm)] - scoreDict[tuple(perm)])
        # Accept or reject?
        unif = numpy.random.uniform()
        if unif <= acceptValue:
            # Accept and transition!
            perm = testperm

        # Print every 100
        if i % 100 == 0:
            print("Iteration #" + str(i) + ":\n" + decrypt(perm, inputText))
    