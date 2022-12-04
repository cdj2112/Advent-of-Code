f = open("./input.txt", "r")

seedNum = f.read()

def describeNumber(num):
	currDigit = ""
	count = 0
	newNum = ""

	for d in num:
		if d != currDigit:
			if len(currDigit):
				newNum += str(count) + currDigit
			currDigit = d
			count = 0

		count += 1

	newNum += str(count) + currDigit

	return newNum

for i in range(50):
	seedNum = describeNumber(seedNum)

print(len(seedNum))