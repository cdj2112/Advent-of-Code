f = open("./input.txt", "r")

cmd = f.read().split("\n")

cycleNumber = 0
register = 1

cmdIndex = 0
cmdDelay = 0

strength = 0
crt = ""

while cycleNumber < 240:
	c = cmd[cmdIndex].split()
	if c[0] == "addx" and cmdDelay == 0:
		cmdDelay = 2

	if c[0] =="addx":
		cmdDelay -= 1

	horz = cycleNumber % 40
	crt += "#" if abs(horz - register) <= 1 else "."

	cycleNumber += 1

	if cycleNumber % 40 == 0:
		crt += "\n"

	if cycleNumber % 20 == 0 and (cycleNumber / 20) % 2 == 1:
		strength += cycleNumber * register
		print(cycleNumber, register)

	if cmdDelay == 0:
		if c[0] == "addx":
			register += int(c[1])
		print(c, cycleNumber + 1, register)
		cmdIndex += 1

print(strength)
print(crt)