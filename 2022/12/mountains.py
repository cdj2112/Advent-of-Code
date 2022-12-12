f = open("./input.txt", "r")

mountains = f.read().split("\n")

sx = 0
sy = 0
ex = 0
ey = 0

for i in range(len(mountains)):
	for j in range(len(mountains[i])):
		if mountains[i][j] ==  "S":
			sx = j
			sy = i
		if mountains[i][j] ==  "E":
			ex = j
			ey = i

dirr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
distTo = [[-1 for x in range(len(mountains[0]))] for y in range(len(mountains))]

stepCoord = set()

stepCoord.add(str(sx)+", "+str(sy))
distTo[sy][sx] = 0

for x in range(len(mountains[0])):
	for y in range(len(mountains)):
		if mountains[y][x] == "a":
			stepCoord.add(str(x)+", "+str(y))
			distTo[y][x] = 0

for s in range(1, len(mountains[0]) * len(mountains)):
	newStep = set()
	for cstr in stepCoord:
		c = [int(k) for k in cstr.split(", ")]
		cH = ord(mountains[c[1]][c[0]]) - ord("a") if (c[0] != sx or c[1] != sy) else 0
		for d in range(4):
			[dx, dy] = dirr[d]
			nx = dx + c[0]
			ny = dy + c[1]

			xEdge = nx < 0 or nx >= len(mountains[0])
			yEdge = ny < 0 or ny >= len(mountains)
			if(xEdge or yEdge):
				continue

			nH = ord(mountains[ny][nx]) - ord("a") if (c[0] != ex or c[1] != ey) else ord("z") - ord("a")
			if distTo[ny][nx] == -1 and nH <= cH + 1:
				newStep.add(str(nx)+", "+str(ny))
				distTo[ny][nx] = s

	if str(ex)+", "+str(ey) in newStep:
		print("Fin", s)
		break
	else:
		print(s, len(newStep))
		stepCoord = newStep