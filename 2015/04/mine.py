import hashlib

f = open("./input.txt", "r")

key = f.read()

found = False
suffix = 1

while not found:
	trial = key + str(suffix)

	hashFn = hashlib.new('md5')
	hashFn.update(trial.encode())
	result = hashFn.hexdigest()
	
	found = result[0:6] == '000000'

	suffix += 1

print(suffix - 1)


