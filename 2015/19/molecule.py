import re
import math

f = open("./input.txt", "r")

[repStr, mol] = f.read().split("\n\n")

replacements = [[e[0], e[2]] for e in [r.split() for r in repStr.split("\n")]]

possible = set()

for r in replacements:
	finds = re.finditer(r[0], mol)
	for f in finds:
		preffix = mol[:f.start()]
		suffix = mol[f.end():]
		newMol = preffix + r[1] + suffix
		possible.add(newMol)

print(len(possible))
print(len(mol))