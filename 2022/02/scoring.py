f = open("./input.txt", "r")

stratagies = f.read().split('\n')

#firstMove = [ 'A', 'B', 'C']
#secondMove = [ 'X', 'Y', 'Z']
points = 0
points2 = 0

for game in stratagies:
	moves = game.split()

	result = (ord(moves[1]) - ord(moves[0]) - 1) % 3
	resultPoints = 3 * result
	movePoints = ord(moves[1]) - ord('X') + 1
	points += resultPoints + movePoints

	resultPoints2 = 3 * (ord(moves[1]) - ord('X'))
	movePoints2 = (ord(moves[0]) - ord('A') + ord(moves[1]) - ord('X') + 2) % 3 + 1
	points2 += resultPoints2 + movePoints2


print(points, points2)