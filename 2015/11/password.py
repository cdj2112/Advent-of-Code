f = open("./input.txt", "r")

currPass = f.read()

numPass = [0] * len(currPass)

for l, i in zip(currPass, range(len(numPass))):
	numPass[i] = ord(l) - ord("a")

