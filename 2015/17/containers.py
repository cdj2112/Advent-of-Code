f = open("./input.txt", "r")

contStr = f.read().split("\n")
contain = [int(c) for c in contStr]

print(len(contain))

volume = 150
combIdx = 0

valid = [0] * len(contain)

while combIdx < pow(2, len(contain)):
	held = 0
	numUsed = 0

	for i in range(len(contain)):
		used = ((combIdx - combIdx % pow(2, i)) / pow(2, i)) % 2
		held += used * contain[i]
		numUsed += int(used)

	if numUsed >= 1:
		valid[numUsed - 1] += 1 if held == volume else 0

	combIdx += 1

print(sum(valid), valid)