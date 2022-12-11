import math

f = open("./input.txt", "r")

rows = f.read().split("\n")

for i in range(100):
	newRows = []

	for r in range(len(rows)):
		newRow = ""

		for c in range(len(rows[0])):
			neighbors = 0

			for d in range(9):
				x = c + d % 3 - 1
				y = r + math.floor(d / 3) - 1
				if x < 0 or y < 0 or x == len(rows[0]) or y == len(rows) or (x == c and y == r):
					continue
				if rows[y][x] == "#":
					neighbors += 1

			stayalive = (rows[r][c] == "#" and neighbors >= 2 and neighbors <= 3)
			comealive = (rows[r][c] == "." and neighbors == 3)
			corner = (r == 0 or r == len(rows) - 1) and (c == 0 or c == len(rows[0]) - 1)
			newRow += ("#" if stayalive or comealive or corner else ".")

		newRows.append(newRow)

	rows = newRows

print(sum([sum([1 if c == "#" else 0 for c in r]) for r in rows]))