import math

f = open("./input.txt", "r")

cmds = f.read().split("\n")

directorySize = dict()
filePath = []

for c in cmds:
	if "$ cd" in c:
		mDir = c[5:]
		if mDir != "..":
			filePath.append(mDir)
			fileKey = '~'.join(filePath)
			directorySize[fileKey] = 0
		else:
			filePath.pop(-1)
	elif c[0] != "$" and "dir" not in c:
		fileSize = int(c.split()[0])
		for i in range(1, len(filePath) + 1):
			key = "~".join(filePath[0:i])
			directorySize[key] += fileSize

print(sum([(directorySize[f] if directorySize[f] <= 100000 else 0) for f in directorySize]))

totalSize = directorySize["/"]
toFreeSpace = totalSize - 40000000
print(min([directorySize[d] if directorySize[d] >= toFreeSpace else math.inf for d in directorySize]))