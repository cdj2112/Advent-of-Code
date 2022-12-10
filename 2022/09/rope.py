
f = open("./input.txt", "r")

moves = f.read().split("\n")

positions = set()
sPositions = set()

headPos = [0, 0]
tailPos = [0, 0]

snakePos = [[0, 0] for i in range(10)]

positions.add(str(tailPos[0])+' '+str(tailPos[1]))
sPositions.add(str(snakePos[-1][0])+' '+str(snakePos[-1][1]))

for m in moves:
	[direc, ls] = m.split()
	leng = int(ls)
	for l in range(leng):
		if direc == "U":
			headPos[1] += 1
			snakePos[0][1] += 1
		elif direc == "R":
			headPos[0] += 1
			snakePos[0][0] += 1
		elif direc == "D":
			headPos[1] += -1
			snakePos[0][1] += -1
		else:
			headPos[0] += -1
			snakePos[0][0] += -1

		if abs(headPos[0] - tailPos[0]) >= 2 or abs(headPos[1] - tailPos[1]) >= 2:
			if direc == "U":
				tailPos = [headPos[0], headPos[1] - 1]
			elif direc == "R":
				tailPos = [headPos[0] - 1, headPos[1]]
			elif direc == "D":
				tailPos = [headPos[0], headPos[1] + 1]
			else:
				tailPos = [headPos[0] + 1, headPos[1]]

		for i in range(1, len(snakePos)):
			pull = snakePos[i - 1]
			follow = snakePos[i]

			if abs(pull[0] - follow[0]) >= 2 and abs(pull[1] - follow[1]) >= 2:
				if pull[0] > follow[0]:
					snakePos[i][0] = pull[0] - 1
				else:
					snakePos[i][0] = pull[0] + 1

				if pull[1] > follow[1]:
					snakePos[i][1] = pull[1] - 1
				else:
					snakePos[i][1] = pull[1] + 1
			elif abs(pull[0] - follow[0]) >= 2:
				if pull[0] > follow[0]:
					snakePos[i] = [pull[0] - 1, pull[1]]
				else:
					snakePos[i] = [pull[0] + 1, pull[1]]
			elif abs(pull[1] - follow[1]) >= 2:
				if pull[1] > follow[1]:
					snakePos[i] = [pull[0], pull[1] - 1]
				else:
					snakePos[i] = [pull[0], pull[1] + 1]

		positions.add(str(tailPos[0])+' '+str(tailPos[1]))
		sPositions.add(str(snakePos[-1][0])+' '+str(snakePos[-1][1]))

print(len(positions), len(sPositions))