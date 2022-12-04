import math

f = open("./input.txt", "r")

routes = f.read().split("\n")

graph = {}

for r in routes:
	parts = r.split()
	if parts[0] not in graph:
		graph[parts[0]] = {}
	if parts[2] not in graph:
		graph[parts[2]] = {}

	graph[parts[0]][parts[2]] = int(parts[4])
	graph[parts[2]][parts[0]] = int(parts[4])

def findShortest(loc, path):
	shortest = math.inf
	for l in graph[loc]:
		if l in path:
			continue
		newPath = path + loc
		shortest = min(findShortest(l, newPath) + graph[loc][l], shortest)

	if shortest == math.inf:
		shortest = 0

	return shortest

def findLongest(loc, path):
	longest = 0
	for l in graph[loc]:
		if l in path:
			continue
		newPath = path + loc
		longest = max(findLongest(l, newPath) + graph[loc][l], longest)

	return longest

finalShortest = math.inf
finalLongest = 0
for start in graph:
	finalShortest = min(findShortest(start, ""), finalShortest)
	finalLongest = max(findLongest(start, ""), finalLongest)

print(finalShortest, finalLongest)