f = open("./input.txt", "r")

directions = f.read()

houses = {"0 0"}
roboHouses = {"0 0"}

currLoc = [0, 0]
realLoc = [0, 0]
roboLoc = [0, 0]

i = 0

for card in directions:
	nextToMove = realLoc if i % 2 == 0 else roboLoc

	if card == '^':
		currLoc[1] += 1
		nextToMove[1] += 1
	elif card == 'v':
		currLoc[1] += -1
		nextToMove[1] += -1
	elif card == '>':
		currLoc[0] += 1
		nextToMove[0] += 1
	else:
		currLoc[0] += -1
		nextToMove[0] += -1

	houses.add(' '.join([str(coord) for coord in currLoc]))
	roboHouses.add(' '.join([str(coord) for coord in nextToMove]))
	i += 1

print(len(houses), len(roboHouses))