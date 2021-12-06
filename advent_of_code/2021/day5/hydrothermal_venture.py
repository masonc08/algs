import re


def part1():
    with open('advent_of_code/2021/day5/hydrothermal_venture.txt') as r:
        M = [[0]*1000 for _ in range(1000)]
        for line in r:
            x1, y1, x2, y2 = tuple(map(int, re.split(r",|\s->\s", line.strip())))
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    M[x1][i] += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    M[i][y1] += 1
        return sum(sum(v > 1 for v in row) for row in M)

def part2():
    with open('advent_of_code/2021/day5/hydrothermal_venture.txt') as r:
        M = [[0]*1000 for _ in range(1000)]
        for line in r:
            x1, y1, x2, y2 = tuple(map(int, re.split(r",|\s->\s", line.strip())))
            (x1, y1), (x2, y2) = sorted(((x1, y1), (x2, y2)))
            if x1 == x2:
                for i in range(y1, y2+1):
                    M[x1][i] += 1
            elif y1 == y2:
                for i in range(x1, x2+1):
                    M[i][y1] += 1
            else:
                if y1 <= y2:
                    for i, j in zip(range(x1, x2+1), range(y1, y2+1)):
                        M[i][j] += 1
                else:
                    for i, j in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                        M[i][j] += 1
        return sum(sum(v > 1 for v in row) for row in M)
