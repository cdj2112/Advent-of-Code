f = open("./input.txt", "r")

signal = f.read()

packetSize = 14

for i in range(packetSize - 1, len(signal)):
	packet = signal[i - packetSize + 1: i + 1]
	safe = True
	for j in range(packetSize - 1):
		c = packet[j]
		if c in packet[j + 1:]:
			safe = False
	if safe:
		print(i + 1)
		break