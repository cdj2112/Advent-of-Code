f = open("./input.txt", "r")

cubes = f.read().split("\n")

checked = []
surfA = 0

mD = [0] * 6

for c in cubes:
	co = [int(a) for a in c.split(",")]
	colide = 6

	mD = [max(mD[0], co[0]), min(mD[1], co[0]), \
	max(mD[2], co[1]), min(mD[3], co[1]), \
	max(mD[4], co[2]), min(mD[5], co[2])]

	for d in range(6):
		v = [0, 0, 0]
		s = d % 2 * 2  - 1
		i = int((d - d % 2) / 2)

		v[i] = s

		n = [str(co[i] + v[i]) for i in range(3)]

		if ','.join(n) in checked:
			colide -= 2

	surfA += colide
	checked.append(c)

print(surfA)

internAir = set()
externalAir = set()

for x in range(mD[1], mD[0] + 1):
	for y in range(mD[3], mD[2] + 1):
		for z in range(mD[5], mD[4] + 1):
			startStr = ','.join([str(c) for c in [x,y,z]])
			if startStr in internAir or \
			startStr in externalAir \
			or startStr in cubes:
				continue

			blobSet = set()
			blobSet.add(startStr)

			newBlock = [[x,y,z]]
			isIntern = True
			while len(newBlock) > 0 and isIntern:
				nextBlock = []
				for b in newBlock:
					for d in range(6):
						v = [0, 0, 0]
						s = d % 2 * 2  - 1
						i = int((d - d % 2) / 2)

						v[i] = s

						n = [b[i] + v[i] for i in range(3)]
						nStr = ','.join([str(c) for c in n])

						if nStr not in cubes \
						and nStr not in blobSet \
						and nStr not in internAir:
							nextBlock.append(n)
							blobSet.add(nStr)
						elif nStr in externalAir \
						or n[0] not in range(mD[1], mD[0] + 1) \
						or n[1] not in range(mD[3], mD[2] + 1) \
						or n[2] not in range(mD[5], mD[4] + 1):
							blobSet.add(nStr)
							isIntern = False

				newBlock = nextBlock

			if isIntern:
				internAir.update(blobSet)
			else:
				externalAir.update(blobSet)

print(len(cubes), len(internAir), len(externalAir), mD)
extSA = 0
for c in cubes:
	co = [int(a) for a in c.split(",")]
	colide = 6

	for d in range(6):
		v = [0, 0, 0]
		s = d % 2 * 2  - 1
		i = int((d - d % 2) / 2)

		v[i] = s

		n = [str(co[i] + v[i]) for i in range(3)]

		if ','.join(n) in internAir or ','.join(n) in cubes:
			colide -= 1

	extSA += colide

print(extSA)