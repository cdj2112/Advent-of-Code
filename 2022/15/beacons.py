f = open("./input.txt", "r")

beacons = f.read().split("\n")

sensorData = []
beaconData = []

minX = 0
maxX = 0
minY = 0
maxY = 0

maxDist = 0
for b in beacons:
	info = b.split()
	sX = int(info[2][2:-1])
	sY = int(info[3][2:-1])

	bX = int(info[8][2:-1])
	bY = int(info[9][2:])

	matDist = abs(sX - bX) + abs(sY - bY)

	maxX = max(maxX, sX + matDist)
	maxY = max(maxY, sY + matDist)
	minX = min(minX, sX - matDist)
	minY = min(minY, sY - matDist)

	sensorData.append((sX, sY))
	beaconData.append((bX, bY))

#grid = [["." for x in range(maxX + 1)] for y in range(maxY + 1)]
#for s in sensorData:
#	grid[s[1]][s[0]] = "S"
#	grid[s[3]][s[2]] = "B"


yCoord = 2000000
count = 0
print(minX, maxX)

for x in range(minX, maxX + 1):
	if (x, yCoord) in beaconData:
		print("skip")
		continue
	for (s, b) in zip(sensorData, beaconData):
		matDist = abs(s[0] - b[0]) + abs(s[1] - b[1])
		dist = abs(s[0] - x) + abs(s[1] - yCoord)

		if dist <= matDist:
			count += 1
			break

print(count)

def checkBeacons(yc, interval, sensorData, beaconData):
	if interval[0] == interval[1]:
		return []
	elif len(sensorData) == 0:
		return interval

	i = 0
	while i < len(sensorData):
		s = sensorData[i]
		b = beaconData[i]
		matDist = abs(s[0] - b[0]) + abs(s[1] - b[1])
		if matDist - abs(s[1] - yc) < 0:
			i += 1
			continue
		minCX = s[0] - (matDist - abs(s[1] - yc))
		maxCX = s[0] + (matDist - abs(s[1] - yc)) + 1

		total = []
		if minCX > interval[0]:
			left = checkBeacons(yc, [interval[0], min(minCX, interval[1])], sensorData[i + 1:], beaconData[i + 1:])
			if(len(left) > 0):
				total.extend(left)
		
		if maxCX < interval[1]:
			right = checkBeacons(yc, [max(maxCX, interval[0]), interval[1]], sensorData[i + 1:], beaconData[i + 1:])
			if(len(right) > 0):
				total.extend(right)

		return total

	return interval

dimMax = 4000000
for y in range(dimMax + 1):
	poss = checkBeacons(y, [0, dimMax + 1], sensorData, beaconData)
	if len(poss) > 0:
		print(poss, y, poss[0] * dimMax + y)