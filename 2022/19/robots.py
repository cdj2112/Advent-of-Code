import math

f = open("./input.txt", "r")

robots = f.read().split("\n")

blueprintStats = []
for r in robots:
	b = r.split(": ")[1].split(". ")
	blueprintStats.append([int(b[0].split()[-2]), int(b[1].split()[-2]), int(b[2].split()[-5]),\
	int(b[2].split()[-2]), int(b[3].split()[-5]), int(b[3].split()[-2])])

minutes = 32
print(blueprintStats)
def sToStr(state):
	return ','.join([str(s) for s in state])


maxGeo = [0] * len(blueprintStats)
for (b, bi) in zip(blueprintStats[:3], range(3)):
	states = [[1, 0, 0, 0, \
	0, 0, 0, 0, \
	minutes]]
	onClock = True
	while len(states):
		mFC = 0
		newStates = []
		coveredState = set()
		print(bi, states[0][8], len(states))
		for s in states:
			if s[8] == 0:
				maxGeo[bi] = max(maxGeo[bi], s[7])
				continue
			#Time
			s[8] -= 1

			#Collecting
			for i in range(4):
				s[i + 4] += s[i]

			bPlans = [[0, 0, 0, 0]]
			if s[4] - s[0] >= b[0] and s[0] < max(b[1], b[2], b[4]):
				bPlans.append([1, 0, 0, 0])
			if s[4] - s[0] >= b[1] and s[1] < b[3]:
				bPlans.append([0, 1, 0 ,0])
			if s[4] - s[0] >= b[2] and s[5] - s[1] >= b[3] and s[2] < b[5]:
				bPlans.append([0, 0, 1 ,0])
			if s[4] - s[0] >= b[4] and s[6] - s[2] >= b[5]:
				bPlans.append([0, 0, 0 ,1])

			for bp in bPlans:
				ns = s.copy()

				for i in range(4):
					ns[i] += bp[i]

				ns[4] -= b[0] * bp[0] + b[1] * bp[1] + b[2] * bp[2] + b[4] * bp[3]
				ns[5] -= b[3] * bp[2]
				ns[6] -= b[5] * bp[3]

				nsStr = sToStr(ns)
				if nsStr not in coveredState:
					mFC = max(mFC, ns[7] + ns[8] * ns[3])
					newStates.append(ns)
					coveredState.add(nsStr)

		states = []
		for ns in newStates:
			maxFC = ns[7] + ns[8] * ns[3] + ns[8] * (ns[8] - 1) / 2
			if maxFC >= mFC:
				states.append(ns)
		#print("end", len(states))

print(maxGeo[0] * maxGeo[1] * maxGeo[2])