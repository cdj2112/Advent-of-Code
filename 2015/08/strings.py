import re

f = open("./input.txt", "r")

strings = f.read().split("\n")

escape = "(\\\\x[0-9,a-f]{2}|\\\\\\\\|\\\\\\\")"
finder = "(\\\"|\\\\)"

tChar = 0
pChar = 0
nChar = 0

for s in strings:
	a = s[1:-1]
	sChars = re.findall(escape, a)
	diff = len(sChars) - sum(len(c) for c in sChars)

	cChars = re.findall(finder, s)


	tChar += len(s)
	pChar += len(a) + diff
	nChar += len(s) + len(cChars) + 2

print(tChar - pChar, nChar - tChar)