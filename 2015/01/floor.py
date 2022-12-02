f = open("./input.txt", "r")

floors = f.read()

currFloor = 0
basement = 0
idx = 0

for cmd in floors:
	currFloor += 1 if cmd == '(' else -1
	idx += 1

	if currFloor < 0 and basement == 0:
		basement = idx

print(currFloor, basement) 