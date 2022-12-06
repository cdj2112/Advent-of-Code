f = open("./input.txt", "r")

currPass = f.read()

numPass = [0] * len(currPass)

for l, i in zip(currPass, range(len(numPass))):
	numPass[i] = ord(l) - ord("a")

bannedLetter = [8, 11, 14]

def incPass(currPass):
	idx = len(currPass) - 1

	currPass[idx] = (currPass[idx] + 1) % 26

	while currPass[idx] == 0:
		idx -= 1
		currPass[idx] = (currPass[idx] + 1) % 26

	detect = []
	for i in range(len(currPass)):
		if currPass[i] in bannedLetter:
			detect.append(i)

	if(len(detect)):
		problem = detect[0]
		currPass[problem] = (currPass[problem] + 1) % 26
		for i in range(problem + 1, len(currPass)):
			currPass[i] = 0

	return currPass

def checkPass(currPass):
	doubles = []
	for i in range(len(currPass) - 1):
		if currPass[i] == currPass[i + 1]:
			doubles.append(i)
	doubleCheck = (len(doubles) == 2 and doubles[0] + 1 != doubles[1]) or len(doubles) > 2

	accendingTriple = []
	for i in range(len(currPass) - 2):
		if currPass[i] + 1 == currPass[i + 1] and currPass[i + 1] + 1 == currPass[i + 2]:
			accendingTriple.append(i)
	accendingCheck = len(accendingTriple) > 0

	return doubleCheck and accendingCheck

def findNextPass(numPass):
	while not checkPass(numPass):
		numPass = incPass(numPass)
	return numPass

numPass = findNextPass(numPass)
print(''.join([chr(v + ord('a')) for v in numPass]))

numPass = incPass(numPass)
numPass = findNextPass(numPass)
print(''.join([chr(v + ord('a')) for v in numPass]))