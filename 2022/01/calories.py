f = open("./input.txt", "r")

elves = f.read().split('\n\n')

bestSums = [ 0, 0, 0 ]
for elf in elves:
	items = elf.split('\n')
	itemSum = 0

	for item in items:
		itemSum += int(item)

	pos = [i for i in range(3) if itemSum > bestSums[i]]
	if len(pos) > 0:
		bestSums.insert(pos[0], itemSum)
		bestSums.pop(-1)

print(bestSums, sum(bestSums))