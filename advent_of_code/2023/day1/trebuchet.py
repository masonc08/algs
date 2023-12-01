def part1():
    with open("in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    sol = 0
    for line in lines:
        first = last = None
        for c in line:
            if c.isnumeric():
                if first is None:
                    first = c
                else:
                    last = c
        if first is None:
            first = 0
        if last is None:
            last = first
        sol += int(first+last)
    return sol

def part2():
    with open("advent_of_code/2023/day1/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    sol = 0
    substrs = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    translate = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }
    def first_sbs(s, rev=False):
        l = []
        for subs in substrs:
            if rev:
                subs = subs[::-1]
            if subs in s:
                if not rev:
                    l.append((s.index(subs), subs))
                if rev:
                    l.append((s.index(subs), subs[::-1]))
        l.sort()
        return translate[l[0][1]] if l else "0"

    for line in lines:
        first = first_sbs(line)
        last = first_sbs(line[::-1], rev=True)
        sol += int(first + last)
        print(first, last)
    return sol




print(part2())
