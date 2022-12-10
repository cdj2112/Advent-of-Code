f = open("./input.txt", "r")

properties = f.read().split("\n")
values = []
for p in properties:
	v = p.split(",")
	values.append([int(v[i].split()[-1]) for i in range(5)])

teaspoons = 100

bars = [i for i in range(len(properties) - 1)]

def nextBars(currBars):
	valid = False
	for i in range(len(currBars) - 1, -1, -1):
		currBars[i] += 1
		for j in range(i + 1, len(currBars)):
			currBars[j] = currBars[i] + j - i
		if currBars[i] < teaspoons + i:
			valid = True
			break

	return currBars if valid else None

bestScore = 0

#for i in range(2000): 
while bars != None:
	mixP = [0, 0, 0, 0, 0]

	for i in range(len(bars) + 1):
		start = -1 if i == 0 else bars[i - 1]
		end = teaspoons + len(bars) if i == len(bars) else bars[i]
		total = end - start - 1

		for m in range(len(mixP)):
			mixP[m] += total * values[i][m]

	#print(bars, mixP)
	if (mixP[4] == 500):
		bestScore = max(bestScore, max(mixP[0], 0) * max(mixP[1], 0) * max(mixP[2], 0) * max(mixP[3], 0))
	bars = nextBars(bars)

print(bestScore)