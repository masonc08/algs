from itertools import combinations


def load_sky():
    with open("advent_of_code/2023/day11/in.txt") as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]

def get_empty_rows(m):
    return set(
        i
        for i, line in enumerate(m)
        if all(v == "." for v in line)
    )

def get_stars(sky):
    return set(
        (i, j)
        for i, line in enumerate(sky)
        for j, v in enumerate(line)
        if v == "#"
    )

def part1():
    sky = load_sky()
    empty_rows = get_empty_rows(sky)
    empty_cols = get_empty_rows([list(x) for x in zip(*sky)])
    stars = get_stars(sky)
    sol = 0
    for (ai, aj), (bi, bj) in combinations(stars, 2):
        dist = abs(bi-ai) + abs(bj-aj)
        for row_i in empty_rows:
            lo, hi = min(ai, bi), max(ai, bi)
            if lo < row_i < hi:
                dist += 1000000-1
        for col_j in empty_cols:
            lo, hi = min(aj, bj), max(aj, bj)
            if lo < col_j < hi:
                dist += 1000000-1
        sol += dist
    return sol


print(part1())