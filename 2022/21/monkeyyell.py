f = open("./input.txt", "r")

yells = f.read().split("\n")

yEq = dict()
for y in yells:
	[k, eq] = y.split(": ")

	if ord(eq[0]) >= ord("0") and ord(eq[0]) <= ord("9"):
		yEq[k] = float(eq)
	else:
		yEq[k] = eq

values = dict()
def findValue(name):
	if name in values:
		return values[name]

	if type(yEq[name]) is float:
		values[name] = yEq[name]
		return yEq[name]

	[a, op, b] = yEq[name].split()
	v1 = findValue(a)
	v2 = findValue(b)

	val = 0
	if op == "+":
		val = v1 + v2
	elif op == "-":
		val = v1 - v2
	elif op == "*":
		val = v1 * v2
	else:
		val = v1 / v2

	values[name] = val
	return val

print(findValue("root"))

chain = []
links = ["humn"]
while len(links):
	newLinks = []
	for l in links:
		for y in yEq:
			eq = yEq[y]
			if type(eq) is not float and l in eq and y not in newLinks:
				newLinks.append(y)

	chain.append(links)
	links = newLinks

def reverseValue(name, v):
	if name == "humn":
		print(v)
		return

	[a, op, b] = yEq[name].split()

	if a in cP:
		f = findValue(b)
		if op == "+":
			reverseValue(a, v - f)
		elif op == "-":
			reverseValue(a, v + f)
		elif op == "*":
			reverseValue(a, v / f)
		else:
			reverseValue(a, v * f)
	else:
		f = findValue(a)
		if op == "+":
			reverseValue(b, v - f)
		elif op == "-":
			reverseValue(b, f - v)
		elif op == "*":
			reverseValue(b, v / f)
		else:
			reverseValue(b, f / v)

cP = [c[0] for c in chain]

[a, op, b] = yEq["root"].split()

v = 0
if a in chain[-2]:
	v = findValue(b)
	reverseValue(a, v)
else:
	v = findValue(a)
	reverseValue(b, v)

