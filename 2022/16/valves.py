import math

f = open("./input.txt", "r")

valves = f.read().split("\n")

valveGraph = dict()
nodeValves = []

for v in valves:
	info = v.split()
	name = info[1]
	rate = int(info[4].split("=")[1][:-1])
	leads = [i[:-1] for i in info[9:-1]]
	leads.append(info[-1])

	obj = dict()
	obj["rate"] = rate
	if rate > 0:
		nodeValves.append(name)
	obj["tunnels"] = leads

	valveGraph[name] = obj

position = "AA"
minutes = 26

shortPath = dict()

def findShortestPath(start, end):
	if start == end:
		return [start]
	elif start+end in shortPath:
		return shortPath[start+end]
	elif end+start in shortPath:
		return shortPath[end+start]

	found = False

	paths = [[start]]
	visited = set()
	visited.add(start)

	while not found:
		newPaths = []
		for p in paths:
			currPos = p[-1]
			for n in valveGraph[currPos]["tunnels"]:
				if n in visited:
					continue
				if n == end:
					found = True
					p.append(n)
					shortPath[start+end] = p
					return p
				else:
					np = p.copy()
					np.append(n)
					newPaths.append(np)

		paths = newPaths

def findOptimalPaths(start, exclude):
	optimal = dict()
	for v in nodeValves:
		if v in exclude:
			continue
		dist = len(findShortestPath(start, v))
		rate = valveGraph[v]["rate"]
		canAdd = True
		toPop = []
		for o in optimal:
			ov = optimal[o]
			odist = ov[0]
			orate = ov[1]
			if dist == odist and rate == orate:
				continue
			elif dist <= odist and rate >= orate:
				toPop.append(o)
			elif dist >= odist and rate <= orate:
				canAdd = False

		for p in toPop:
			optimal.pop(p)
		if canAdd:
			optimal[v] = (dist, rate)
	return optimal

optPath = dict()

def bestOptimizedDist(start, dest, bug, excludelist):
	if start == dest:
		return 0
	elif start+dest in optPath:
		return optPath[start+dest]
	elif dest+start in optPath:
		return optPath[dest+start]

	opt = findOptimalPaths(start, excludelist)
	mindist = math.inf
	for o in opt:
		if opt[o][0] > bug:
			continue
		el = excludelist.copy()
		el.add(o)
		mindist = min(mindist, opt[o][0] + bestOptimizedDist(o, dest, bug - opt[o][0], el))

	if mindist != math.inf:
		optPath[start+dest] = mindist
	return mindist

def doubleOptimal(start, partDest, partDist, excludelist):
	paths = findOptimalPaths(start, excludelist)
	checkPaths = paths
	totalBv = []

	while len(checkPaths) > 0:
		bv = []
		for cp in checkPaths:
			od = bestOptimizedDist(partDest, cp, checkPaths[cp][0], excludelist)
			if od + partDist < checkPaths[cp][0]:
				bv.append(cp)
		totalBv.extend(bv)

		newCheck = dict()
		el = excludelist.copy()
		el.update(totalBv)

		poss = findOptimalPaths(start, el)
		for p in poss:
			if p not in paths and p not in newCheck:
				newCheck[p] = poss[p]

		for nc in newCheck:
			paths[nc] = newCheck[nc]

		checkPaths = newCheck

	return paths



onClock = True
paths = [([position], 0, 30)]
maxPath = ([], 0, 0)
while onClock:
	onClock = False
	newPaths = []
	for p in paths:
		if p[2] <= 0:
			if p[1] >= maxPath[1]:
				maxPath = p
			continue

		currPos = p[0][-1]
		opPaths = findOptimalPaths(currPos, p[0])
		currPressure = sum([valveGraph[v]["rate"] for v in p[0]])

		if len(opPaths) == 0:
			p[1] += p[2] * currPressure
			p[2] = 0
			if p[1] >= maxPath[1]:
				maxPath = p

		onClock = True

		for op in opPaths:
			budget = min(opPaths[op][0], p[2])
			pressureGain = currPressure * budget

			newP = p[0].copy()
			newP.append(op)

			newPaths.append((newP, p[1] + pressureGain, p[2] - budget))

	paths = newPaths
	print(len(paths))

print(maxPath)

paths = [([position], [position], "b", 0, 0, 26)]
maxPath = ([], [], "b", 0, 0, 0)

while len(paths) > 0:
	newPaths = []
	for p in paths:
		if p[5] <= 0:
			if p[4] >= maxPath[4]:
				maxPath = p
			continue
		elif p[0][-1] == p[1][-1] and p[0][-1] != "AA":
			continue

		excludelist = set()

		if p[2] == "h":
			excludelist.update(p[0])
			excludelist.update(p[1][:-1])
			opPaths = doubleOptimal(p[0][-1], p[1][-1], p[3], excludelist)
			currPressure = sum([valveGraph[v]["rate"] for v in excludelist])

			if len(opPaths) == 0:
				value = p[4] + p[5] * currPressure
				if value > maxPath[4]:
					maxPath = (p[0], p[1], p[2], p[3], value, 0)
				continue

			for op in opPaths:
				budget = min(opPaths[op][0], p[5], p[3])
				pressureGain = currPressure * budget

				newP = p[0].copy()
				newP.append(op)

				newTime = p[3] - budget
				newTurn = "h" if newTime > 0 else ("b" if p[3] == opPaths[op][0] else "e")
				if newTime == 0:
					newTime = opPaths[op][0] - budget

				newPaths.append((newP, p[1], newTurn, newTime, \
					p[4] + pressureGain, p[5] - budget))
		elif p[2] == "e":
			excludelist.update(p[0][:-1])
			excludelist.update(p[1])
			opPaths = doubleOptimal(p[1][-1], p[0][-1], p[3], excludelist)
			currPressure = sum([valveGraph[v]["rate"] for v in excludelist])
				 
			if len(opPaths) == 0:
				value = p[4] + p[5] * currPressure
				if value > maxPath[4]:
					maxPath = (p[0], p[1], p[2], p[3], value, 0)
				continue

			for op in opPaths:
				budget = min(opPaths[op][0], p[5], p[3])
				pressureGain = currPressure * budget

				newP = p[1].copy()
				newP.append(op)

				newTime = p[3] - budget
				newTurn = "e" if newTime > 0 else ("b" if p[3] == opPaths[op][0] else "h")
				if newTime == 0:
					newTime = opPaths[op][0] - budget
					
				newPaths.append((p[0], newP, newTurn, newTime, \
					p[4] + pressureGain, p[5] - budget))
		else:
			excludelist.update(p[0])
			excludelist.update(p[1])
			opPaths = doubleOptimal(p[0][-1], p[1][-1], p[3], excludelist)
			opPaths2 = doubleOptimal(p[1][-1], p[0][-1], p[3], excludelist)
			currPressure = sum([valveGraph[v]["rate"] for v in excludelist])

			if len(opPaths) == 0:
				value = p[4] + p[5] * currPressure
				if value > maxPath[4]:
					maxPath = (p[0], p[1], p[2], p[3], value, 0)
				continue

			for op in opPaths:
				for op2 in opPaths2:
					if op == op2:
						continue

					budget = min(opPaths[op][0], opPaths2[op2][0], p[5])
					pressureGain = currPressure * budget

					newP1 = p[0].copy()
					newP1.append(op)
					newP2 = p[1].copy()
					newP2.append(op2)

					newTime = opPaths[op][0] - opPaths2[op2][0]
					newTurn = "e" if newTime > 0 else ("b" if newTime == 0 else "h")

					newPaths.append((newP1, newP2, newTurn, abs(newTime), \
						p[4] + pressureGain, p[5] - budget))



	paths = newPaths
	print(len(paths))

print(maxPath)