f = open("./input.txt", "r")

shifts = [int(s) for s in  f.read().split("\n")]

num = dict()
base = []

for s in shifts:
	if s not in num:
		base.append(str(s)+"_0")
		num[s] = 1
	else:
		base.append(str(s)+"_"+str(num[s]))
		num[s] += 1

move = base.copy()
key = 811589153

for cyc in range(10):
	for b in base:
		idx = move.index(b)
		[sS, k] = b.split("_")
		s = int(sS) * key
		nIdx = (idx + s) % (len(base) - 1)

		e = move.pop(idx)
		move.insert(nIdx, e)

zIdx = move.index("0_0")
print(key * (int(move[(zIdx + 1000) % len(move)].split("_")[0]) + \
	int(move[(zIdx + 2000) % len(move)].split("_")[0]) + \
	int(move[(zIdx + 3000) % len(move)].split("_")[0])))