f = open("./input.txt", "r")

gifts = f.read().split('\n')

wrapping = 0
ribbon = 0

for size in gifts:
	dim = size.split('x')
	l, w, h = int(dim[0]), int(dim[1]), int(dim[2])
	wrapping += 2 * (l * w + l * h + w * h) + min(l * w, l * h, w * h)
	ribbon += 2 * min(l + w, l + h, w + h) + l * w * h

print(wrapping, ribbon)