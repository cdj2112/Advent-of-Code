f = open("./input.txt", "r")

words = f.read().split("\n")

def checkNice1(prevLetter, letter, state):
	if (prevLetter + letter) in banned:
		state[2] = False

	if prevLetter == letter:
		state[1] = True

	if letter in vowelList:
		state[0] += 1

	return state

def checkNice2(pharse, state):
	currPair = phrase[0:2]

	if currPair in pairs:
		state[0] = True

	if phrase[0] == phrase[2]:
		state[1] = True

	return state

vowelList = ["a", "e", "i", "o", "u"]
banned = ["ab", "cd", "pq", "xy"]

nice = 0
nice2 = 0

for word in words:
	nice1State = [0, False, True]
	nice2State = [False, False]

	prevLetter = word[0]
	if prevLetter in vowelList:
		nice1State[0] += 1

	pairs = set()
	prevPair = ""

	for s in range(0, len(word) - 2):
		phrase = word[s:s + 3]
		letter = phrase[1]

		nice1State = checkNice1(prevLetter, letter, nice1State)
		nice2State = checkNice2(phrase, nice2State)

		if len(prevPair) > 0:
			pairs.add(prevPair)
		prevPair = phrase[0:2]

		prevLetter = letter



	nice1State = checkNice1(prevLetter, word[-1], nice1State)
	if word[-2:] in pairs:
		nice2State[0] = True

	if nice1State[0] >= 3 and nice1State[1] and nice1State[2]:
		nice += 1	
	if nice2State[0] and nice2State[1]:
		nice2 += 1

print(nice, nice2)