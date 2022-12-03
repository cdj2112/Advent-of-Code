import re

f = open("./input.txt", "r")

gates = f.read().split("\n")

parse = "([a-z]{0,})([0-9]{0,})(?: ?)([A-Z]{0,})(?: ?)([a-z]{0,})([0-9]{0,}) -> (.*)"

source = {}
power = {}

for g in gates:
	bits = re.findall(parse, g)[0]
	source[bits[5]] = bits[0:5]
	power[bits[5]] = None

def findPower(key):
	if len(key) == 0:
		return 0
	if power[key] != None:
		return power[key]

	S1 = int(source[key][1]) if len(source[key][1]) else findPower(source[key][0])
	S2 = int(source[key][4]) if len(source[key][4]) else findPower(source[key][3])
	OPP = source[key][2]

	value = 0

	if OPP == "AND":
		value = (S1 & S2) & 0xFFFF
	elif OPP == "OR":
		value = (S1 | S2) & 0xFFFF
	elif OPP == "NOT":
		value = (~S2) & 0xFFFF
	elif OPP == "LSHIFT":
		value = (S1 << S2) & 0xFFFF
	elif OPP == "RSHIFT":
		value = (S1 >> S2) & 0xFFFF
	else:
		value = S1 & 0xFFFF

	power[key] = value	
	return value

firstPower = findPower("a")
print(firstPower)

for p in power:
	power[p] = None

power["b"] = firstPower

print(findPower("a"))
