import statistics


def part1():
    with open('advent_of_code/2021/day7/the_treachery_of_whales.txt') as r:
        li = list(map(int, next(r).strip().split(",")))
    med = round(statistics.median(li))
    return sum(abs(x-med) for x in li)

def part2():
    with open('advent_of_code/2021/day7/the_treachery_of_whales.txt') as r:
        li = list(map(int, next(r).strip().split(",")))
    i, j = 0, max(li)
    dist = lambda x: sum(abs(x-v)*(abs(x-v)+1)//2 for v in li)
    while i < j:
        m = (i+j)//2
        if dist(m) > dist(m+1):
            i = m+1
        else:
            j = m
    return dist(i)

print(part2())
