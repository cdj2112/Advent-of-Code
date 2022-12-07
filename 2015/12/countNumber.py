import re
import json

f = open("./input.txt", "r")

JSONStr = f.read()

numFinder = "-?[0-9]+"

nums = re.findall(numFinder, JSONStr)
numSum = sum([int(n) for n in nums])

print(numSum)

fullObj = json.loads(JSONStr)

def getObjSum(obj):
	otype = type(obj)
	numSum = 0
	if otype is dict:
		for k in obj:
			v = obj[k]
			if v == "red":
				return 0
			else:
				numSum += getObjSum(v)
		return numSum
	elif otype is list:
		for v in obj:
			numSum += getObjSum(v)
		return numSum
	elif otype is int:
		return obj
	else:
		return 0

print(getObjSum(fullObj))