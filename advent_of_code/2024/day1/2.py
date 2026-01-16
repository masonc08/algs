import collections

def part2():
    with open("advent_of_code/2024/day1/in.txt") as f:
        lines = f.readlines()
        lines = [ line.strip() for line in lines ]
    li, ct = [], collections.Counter()
    for line in lines:
        a, b = map(int, line.split())
        li += a,
        ct[b] += 1
    return sum(v*ct[v] for v in li)

print(part2())