import re

f = open("./input.txt", "r")

sues = f.read().split("\n")
sueProp = []

suefind = "Sue [0-9]+: (.*)"

for s in sues:
	prop = re.findall(suefind, s)[0].split(", ")
	tempSue = dict()

	for p in prop:
		[k, vs] = p.split(": ")
		tempSue[k] = int(vs)

	sueProp.append(tempSue)

trueSue = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1,
}

validSues = []
gProp = ["cats", "trees"]
lProp = ["pomeranians", "goldfish"]

for i in range(len(sueProp)):
	s = sueProp[i]
	isSue = True
	for v in trueSue:
		if v not in s:
			continue
		elif v in gProp and s[v] <= trueSue[v]:
			isSue = False
			break
		elif v in lProp and s[v] >= trueSue[v]:
			isSue = False
			break
		elif v not in gProp and v not in lProp and s[v] != trueSue[v]:
			isSue = False
			break

	if isSue:
		validSues.append(i + 1)

print(validSues)