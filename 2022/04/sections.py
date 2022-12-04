f = open("./input.txt", "r")

assignments = f.read().split("\n")

contains = 0
overlap = 0
for a in assignments:
	elves = a.split(',')
	[e11, e12] = elves[0].split("-")
	[e21, e22] = elves[1].split("-")

	if int(e11) <= int(e21) and int(e12) >= int(e22):
		contains += 1
	elif int(e11) >= int(e21) and int(e12) <= int(e22):
		contains +=1

	if int(e12) >= int(e21) and int(e11) <= int(e22):
		overlap +=1
	elif int(e22) >= int(e11) and int(e21) <= int(e12):
		overlap += 1

print(contains, overlap)