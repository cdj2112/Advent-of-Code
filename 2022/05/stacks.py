import re

f = open("./input.txt", "r")

valueFind = "\\[(.)\\]"

[gridStr, moveStr] = f.read().split("\n\n")

moves = moveStr.split("\n")

gridStr += "\n"
rowCount = sum([1 if c == "\n" else 0 for c in gridStr])
rowLen = int(len(gridStr) / rowCount)
numStack = int(rowLen / 4)

grid = [[] for i in range(numStack)]
gridAdv = [[] for i in range(numStack)]

for r in range(rowCount - 2, -1, -1):
	rowStr = gridStr[r * rowLen: (r + 1) * rowLen]
	for s in range(numStack):
		itemStr = rowStr[4 * s: 4 * (s + 1)]
		itemF = re.findall(valueFind, itemStr)
		if len(itemF):
			grid[s].append(itemF[0])
			gridAdv[s].append(itemF[0])

for m in moves:
	words = m.split()
	moveNum = int(words[1])
	fromIdx = int(words[3]) - 1
	toIdx = int(words[5]) - 1

	keep = grid[fromIdx][:-1 * moveNum]
	moved = reversed(grid[fromIdx][-1 * moveNum:])
	grid[fromIdx] = keep
	grid[toIdx].extend(moved)

	keepAdv = gridAdv[fromIdx][:-1 * moveNum]
	movedAdv = gridAdv[fromIdx][-1 * moveNum:]
	gridAdv[fromIdx] = keepAdv
	gridAdv[toIdx].extend(movedAdv)

print(''.join([s[-1] for s in grid]), ''.join([s[-1] for s in gridAdv]))
