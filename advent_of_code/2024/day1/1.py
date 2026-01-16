def part1():
    with open("advent_of_code/2024/day1/in.txt") as f:
        lines = f.readlines()
        lines = [ line.strip() for line in lines ]
    a, b = [], []
    for line in lines:
        a1, b1 = line.split()
        a.append(int(a1))
        b.append(int(b1))
    a.sort(), b.sort()
    return sum(abs(a1-b1) for a1, b1 in zip(a, b))

print(part1())