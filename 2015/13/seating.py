import re
import math

f = open("./input.txt", "r")

rules = f.read().split("\n")

lineParser = "(.*) .* (gain|lose) ([0-9]*) .* to (.*)\\."

parsedRules = [re.findall(lineParser, l)[0] for l in rules]

people = set([p[0] for p in parsedRules])

for p in people:
	parsedRules.append(("You", "gain", "0", p))
	parsedRules.append((p, "gain", "0", "You"))
people.add("You")

def netHappiness(p1, p2):
	h = 0
	for r in parsedRules:
		if (r[0] == p1 and r[3] == p2) or (r[0] == p2 and r[3] == p1):
			h += int(r[2]) if r[1] == "gain" else -1 * int(r[2])
	return h

def findMaxHappiness(tbs, so):
	if len(tbs) == 0:
		h = 0
		for i in range(len(so) - 1):
			p1 = so[i]
			p2 = so[i + 1]
			h += netHappiness(p1, p2)
		h += netHappiness(so[0], so[-1])
		return (h, so)

	bestHapiness = 0
	bestOrder = []
	for p in tbs:
		newSo = so.copy()
		newTbs = tbs.copy()

		newTbs.remove(p)
		newSo.append(p)

		(h, order) = findMaxHappiness(newTbs, newSo)
		if h > bestHapiness:
			bestHapiness = h
			bestOrder = order

	return (bestHapiness, bestOrder)

opt = findMaxHappiness(people, [])
print(opt[0], opt[1])