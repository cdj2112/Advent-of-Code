import math

f = open("./input.txt", "r")

speeds = f.read().split("\n")

time = 2503
distances = dict()
currDistance = dict()
points = dict()

for s in speeds:
	w = s.split()

	name = w[0]
	v = int(w[3])
	p = int(w[6])
	r = int(w[-2])

	d = v * p * math.floor(time / (p + r)) + min(time % (p + r), p) * v
	distances[name] = d
	currDistance[name] = 0
	points[name] = 0

print(max([distances[r] for r in distances]))

for i in range(time):
	bestDistance = -1
	bestDeer = []
	for s in speeds:
		w = s.split()

		name = w[0]
		v = int(w[3])
		p = int(w[6])
		r = int(w[-2])

		currDistance[name] += (v if (i % (p + r)) < p else 0)
		if(currDistance[name] > bestDistance):
			bestDistance = currDistance[name]
			bestDeer = [name]
		elif currDistance[name] == bestDistance:
			bestDeer.append(name)

	for d in bestDeer:
		points[d] += 1

print(max([points[r] for r in points]))