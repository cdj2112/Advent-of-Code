import re
import math

f = open("./input.txt", "r")

monkeyStr = f.read().split("\n\n")
monkeys = []
for ms in monkeyStr:
	lines = ms.split("\n")
	tempMon = dict()

	tempMon["idx"] = int(lines[0].split()[1][0])
	tempMon["items"] = [int(i) for i in lines[1].split(": ")[1].split(", ")]
	tempMon["opp"] = lines[2].split(": ")[1].split("= ")[1].split()
	tempMon["mod"] = int(lines[3].split(": ")[1].split()[2])
	tempMon["iftrue"] = int(lines[4].split(": ")[1].split()[3])
	tempMon["iffalse"] = int(lines[5].split(": ")[1].split()[3])

	monkeys.append(tempMon)

monkeyInsp = [0] * len(monkeys)
print(len(monkeys))

commonMulti = 1
for m in monkeys:
	commonMulti *= m["mod"]

for r in range(10000):
	for m in monkeys:
		while len(m["items"]) > 0:
			monkeyInsp[m["idx"]] += 1
			i = m["items"].pop(0)

			firstVal = i if m["opp"][0] == "old" else int(m["opp"][0])
			secVal = i if m["opp"][2] == "old" else int(m["opp"][2])
			newVal = firstVal
			if m["opp"][1] == "+":
				newVal += secVal
			elif m["opp"][1] == "*":
				newVal *= secVal

			newVal = newVal % commonMulti #math.floor(newVal / 3)
			#print(i, m, newVal)
			tfItem = newVal % m["mod"] == 0
			if tfItem:
				monkeys[m["iftrue"]]["items"].append(newVal)
			else:
				monkeys[m["iffalse"]]["items"].append(newVal)

	if r % 1000 == 0:
		print(r)


M = max(monkeyInsp)
monkeyInsp.remove(M)
m = max(monkeyInsp)

print(M * m)