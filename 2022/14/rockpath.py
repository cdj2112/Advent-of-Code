f = open("./input.txt", "r")

rocks = f.read().split("\n")
maxX = 0
maxY = 0
for r in rocks:
	lines = r.split(" -> ")
	for l in lines:
		[x, y] = l.split(",")
		maxX = max(maxX, int(x))
		maxY = max(maxY, int(y))

grid = [["." for i in range(1000)] for j in range(maxY + 3)]

for r in rocks:
	lines = r.split(" -> ")
	prevX = -1
	prevY = -1
	for l in lines:
		[xstr, ystr] = l.split(",")
		x = int(xstr)
		y = int(ystr)
		if prevX != -1:
			if x == prevX:
				for k in range(min(y, prevY), max(y, prevY) + 1):
					grid[k][x] = "#"
			elif y == prevY:
				for k in range(min(x, prevX), max(x, prevX) + 1):
					grid[y][k] = "#"
		prevX = x
		prevY = y

for x in range(1000):
	grid[-1][x] = "#"

canDrop = True
dropped = 0
print(maxX, maxY)

while canDrop:
	sandCoord = (500, 0)
	dropped += 1
	place = False
	while sandCoord[1] < maxY + 2:
		moved = False
		for i in [0, -1, 1]:
			if (sandCoord[0] + i >= 1000 or sandCoord[0] + i < 0):
				canDrop = False
				print("failure")
				break
			space = grid[sandCoord[1] + 1][sandCoord[0] + i]
			if space == "#" or space == "o":
				continue

			sandCoord = (sandCoord[0] + i, sandCoord[1] + 1)
			moved = True
			break

		if not moved:
			place = True
			grid[sandCoord[1]][sandCoord[0]] = "o"
			break

	if sandCoord[1] == 0:
		canDrop = False

print(dropped)