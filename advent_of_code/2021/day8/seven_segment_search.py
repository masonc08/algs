def part1():
    sol = 0
    with open('advent_of_code/2021/day8/seven_segment_search.txt') as r:
        for line in r:
            for display in line.strip().split(' | ')[1].split():
                if len(display) in {2, 3, 4, 7}:
                    sol += 1
    return sol

def part2():
    sol = 0
    with open('advent_of_code/2021/day8/seven_segment_search.txt') as r:
        for line in r:
            cur = ""
            a, b = line.strip().split(' | ')
            a, b = a.split(), b.split()
            mp = {len(s): set(s) for s in a}
            for display in b:
                display = set(display)
                c1, c2, c3 = len(display), len(display&mp[4]), len(display&mp[2])
                if c1 == 2:
                    cur += '1'
                elif c1 == 3:
                    cur += '7'
                elif c1 == 4:
                    cur += '4'
                elif c1 == 7:
                    cur += '8'
                elif c1 == 5 and c2 == 2:
                    cur += '2'
                elif c1 == 5 and c2 == 3 and c3 == 1:
                    cur += '5'
                elif c1 == 5 and c2 == 3 and c3 == 2:
                    cur += '3'
                elif c1 == 6 and c2 == 4:
                    cur += '9'
                elif c1 == 6 and c2 == 3 and c3 == 1:
                    cur += '6'
                elif c1 == 6 and c2 == 3 and c3 == 2:
                    cur += '0'
            sol += int(cur)
    return sol

print(part2())
