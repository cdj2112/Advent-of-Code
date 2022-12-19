import math

f = open("./input.txt", "r")

jets = f.read()

rotation = ["-", "+", "j", "i", "o"]

stack = [["." for x in range(7)] for y in range(4)]

rocks = 0
top = 0
dropRock = True
jetNum = 0
rockCoord = []

def checkDirection(rock, d):
	direc = []
	if d == "<":
		direc = [-1, 0]
	elif d == ">":
		direc = [1, 0]
	else:
		direc = [0, -1]

	for r in rock:
		nx = r[0] + direc[0]
		ny = r[1] + direc[1]
		if nx < 0 or nx >= 7 or ny < 0:
			return False
		elif stack[ny][nx] == "#":
			return False

	return True

total = 1000000000000
start = True

cycleFound = False
cyclePoints = dict()
cyclicTop = 0

remainRocks = 0
remainderBottom = 0
remainPlaced = 0

while not cycleFound or remainPlaced < remainRocks:
	start = False
	rTop = 0
	if dropRock:
		dropRock = False
		rock = rotation[rocks % 5]
		rockCoord = []
		if rock == "-":
			rTop = 3 + top
			for k in range(4):
				rockCoord.append([k + 2, rTop])
		elif rock =="+":
			rTop = 5 + top
			rockCoord.append([3, rTop - 2])
			for k in range(3):
				rockCoord.append([k + 2, rTop - 1])
			rockCoord.append([3, rTop])
		elif rock == "j":
			rTop = 5 + top
			for k in range(3):
				rockCoord.append([k + 2, rTop - 2])
			for k in range(2):
				rockCoord.append([4, rTop - 1 + k])
		elif rock == "i":
			rTop = 6 + top
			for k in range(4):
				rockCoord.append([2, rTop - 3 + k])
		else:
			rTop = 4 + top
			for j in range(2):
				for k in range(2):
					rockCoord.append([2 + k, rTop - 1 + j])

	if len(stack) - 1 < rTop:
		rowsToAdd = rTop - len(stack) + 1
		for i in range(rowsToAdd):
			stack.append(["." for x in range(7)])

	jet = jets[jetNum % len(jets)]
	canJet = checkDirection(rockCoord, jet)

	jetNum += 1

	if canJet:
		for r in range(len(rockCoord)):
			rockCoord[r][0] = rockCoord[r][0] + (-1 if jet == "<" else 1)

	canFall = checkDirection(rockCoord, "v")

	if canFall:
		for r in range(len(rockCoord)):
			rockCoord[r][1] = rockCoord[r][1] - 1
	else:
		top = max(max([r[1] for r in rockCoord]) + 1, top)
		for r in rockCoord:
			stack[r[1]][r[0]] = "#"
		rocks += 1
		dropRock = True

		if rocks % 10000 == 0:
			print(rocks, rocks % 5, jetNum % len(jets))

		if not cycleFound and rocks % 5 == 0:
			jetMod = jetNum % len(jets)
			if jetMod not in cyclePoints:
				cyclePoints[jetNum % len(jets)] = (rocks, top, stack[top - 1].copy())
			else:
				(cR, cT, cA) = cyclePoints[jetMod]
				bottomRow = cA
				topRow = stack[top - 1]
				colide = sum([1 if bottomRow[i] == topRow[i] else 0 for i in range(7)])
				if colide == 7:
					cycleFound = True
					cycleLength = rocks - cR
					cycleHeight = top - cT

					cyclicTop = math.floor((total - cR) / cycleLength) * cycleHeight + cT
					remainRocks = (total - cR) % cycleLength
					remainderBottom = top
		elif cycleFound:
			remainPlaced += 1


print(cyclicTop + top - remainderBottom)

