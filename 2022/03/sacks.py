f = open("./input.txt", "r")

sacks = f.read().split('\n')

def itemValue(item):
	if ord(item) >= ord("a"):
		return ord(item) - ord("a") + 1
	else:
		return ord(item) - ord("A") + 27

proriSum = 0
elfSum = 0

for comp in sacks:
	sLen = int(len(comp) / 2)
	firstC = comp[0:sLen]
	secondC = comp[sLen:]
	for item in firstC:
		if item in secondC:
			proriSum += itemValue(item)
			break

for i in range(0, int(len(sacks) / 3)):
	firstS = sacks[3 * i]
	secondS = sacks[3 * i + 1]
	thirdS = sacks[3 * i + 2]

	for item in firstS:
		if item in secondS and item in thirdS:
			elfSum += itemValue(item)
			break


print(proriSum, elfSum)