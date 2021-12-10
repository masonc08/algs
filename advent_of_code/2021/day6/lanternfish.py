def part1():
    with open('advent_of_code/2021/day6/lanternfish.txt') as r:
        sol = list(map(int, next(r).strip().split(",")))
    for _ in range(80):
        L = len(sol)
        for i in range(L):
            if sol[i] == 0:
                sol[i] = 6
                sol.append(8)
            else:
                sol[i] -= 1
    return len(sol)

def part2():
    occs = [0]*9
    with open('advent_of_code/2021/day6/lanternfish.txt') as r:
        for v in map(int, next(r).strip().split(",")):            
            occs[v] += 1
    for _ in range(256):
        new = occs[1:]
        new[6] += occs[0]
        new.append(occs[0])
        occs = new
    return sum(new)

print(part2())
