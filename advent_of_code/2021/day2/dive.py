def part1():
    d = h = 0
    with open("dive.txt") as r:
        for line in r:
            direc, v = line.split()
            v = int(v)
            if direc == 'forward':
                h += v
            elif direc == 'up':
                d -= v
            else:
                d += v
    return d*h

def part2():
    d = h = aim = 0
    with open("dive.txt") as r:
        for line in r:
            direc, v = line.split()
            v = int(v)
            if direc == 'forward':
                h += v
                d += aim*v
            elif direc == 'up':
                aim -= v
            else:
                aim += v
    return d*h


print(part2())
