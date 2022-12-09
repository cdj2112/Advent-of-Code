f = open("./input.txt", "r")

treeGrid = f.read().split("\n")

visible = 0
maxVis = 0

for x in range(len(treeGrid[0])):
	for y in range(len(treeGrid)):
		tH = int(treeGrid[y][x])

		viewN = [int(treeGrid[v][x]) for v in range(y)]
		nT = max(viewN) if y > 0 else -1

		viewE = [int(treeGrid[y][h]) for h in range(x + 1, len(treeGrid[0]))]
		eT = max(viewE) if x + 1 < len(treeGrid[0]) else -1

		viewS = [int(treeGrid[v][x]) for v in range(y + 1, len(treeGrid))]
		sT = max(viewS) if y + 1 < len(treeGrid) else -1

		viewW = [int(treeGrid[y][h]) for h in range(x)]
		wT = max(viewW) if x > 0 else -1

		if tH > min(nT, eT, sT, wT):
			visible += 1
		trees = [0] * 4
		for t in reversed(viewN):
			trees[0] +=1
			if(t >= tH):
				break
		for t in viewE:
			trees[1] +=1
			if(t >= tH):
				break
		for t in viewS:
			trees[2] +=1
			if(t >= tH):
				break
		for t in reversed(viewW):
			trees[3] +=1
			if(t >= tH):
				break
		maxVis = max(maxVis, trees[0] * trees[1] * trees[2] * trees[3])
print(visible, maxVis)

