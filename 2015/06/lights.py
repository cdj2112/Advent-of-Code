import re

f = open("./input.txt", "r")

instructions = f.read().split("\n")

lights = [[0 for x in range(1000)] for y in range(1000)]
dimmerLights = [[0 for x in range(1000)] for y in range(1000)]

regex = "(.+?) ([0-9]*,[0-9]*) .* ([0-9]*,[0-9]*)"

for ins in instructions:
	parts = re.findall(regex, ins)[0]

	[left, top] = [int(s) for s in parts[1].split(",")]
	[right, bottom] = [int(s) for s in parts[2].split(",")]

	for x in range(left, right + 1):
		for y in range(top, bottom + 1):
			if parts[0] == "turn on":
				lights[x][y] = 1
				dimmerLights[x][y] += 1
			elif parts[0] == "turn off":
				lights[x][y] = 0
				dimmerLights[x][y] = max(dimmerLights[x][y] - 1, 0)
			else:
				lights[x][y] = (lights[x][y] + 1) % 2
				dimmerLights[x][y] += 2

lightNum = sum(sum(col) for col in lights)
dimLightNum = sum(sum(col) for col in dimmerLights)

print(lightNum, dimLightNum)