def part1():
	with open('sonar_sweep.txt') as r:
		p = int(next(r))
		sol = 0
		for line in r:
			if int(line) > p:
				sol += 1
			p = int(line)
		return sol

def part2():
	with open('sonar_sweep.txt') as r:
		a = int(next(r))
		b = int(next(r))
		c = int(next(r))
		sol = 0
		for line in r:
			x = a+b+c
			y = b+c+int(line)
			a, b, c = b, c, int(line)
			if y > x:
				sol += 1
		return sol
