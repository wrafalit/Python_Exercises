primeslist = []
with open('primenumbers.txt') as primesfile:
	line = primesfile.readline()
	count = 0
	print(line)
	while line:
		primeslist.append(int(line))
		count += 1
		line = primesfile.readline()


print(count)
