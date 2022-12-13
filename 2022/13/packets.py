import ast

f = open("./input.txt", "r")

pairs = f.read().split("\n\n")

def comparePair(lP, rP):
	if type(lP) is int and type(rP) is int:
		return lP - rP
	elif (type(lP) is int and type(rP) is list):
		return comparePair([lP], rP)
	elif (type(lP) is list and type(rP) is int):
		return comparePair(lP, [rP])
	else:
		for i in range(min(len(lP), len(rP))):
			v = comparePair(lP[i], rP[i])
			if v != 0:
				return v
		return len(lP) - len(rP)

idx = 1
sumIdx = 0
noPairs = []

for p in pairs:
	[leftStr, rightStr] = p.split("\n")
	left = ast.literal_eval(leftStr)
	right = ast.literal_eval(rightStr)
	noPairs.append(left)
	noPairs.append(right)

	order = comparePair(left, right)
	if order < 0:
		sumIdx += idx

	idx += 1

print(sumIdx)

noPairs.append([[2]])
noPairs.append([[6]])

for i in range(len(noPairs)):
	item = noPairs[0]
	for j in range(1,len(noPairs) - i):
		order = comparePair(item, noPairs[j])

		if order <= 0:
			item = noPairs[j]
		else:
			temp = noPairs[j]
			noPairs[j] = item
			noPairs[j - 1] = temp 

tIdx = -1
sIdx = -1

for i in range(len(noPairs)):
	if len(noPairs[i]) == 1 and len(noPairs[i][0]) == 1:
		if noPairs[i][0][0] == 2:
			tIdx = i + 1
		elif noPairs[i][0][0] == 6:
			sIdx = i + 1

print(tIdx * sIdx)