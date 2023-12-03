def part1():
    def get_is_safe(i, j):
        if i > 0 and is_symbol(lines[i-1][j]):
            return True
        if i < n-1 and is_symbol(lines[i+1][j]):
            return True
        if is_symbol(lines[i][j]):
            return True
        return False

    with open("advent_of_code/2023/day3/in.txt") as f:
        lines = f.readlines()
    lines = [ line.strip() for line in lines ]
    n, m = len(lines), len(lines[0])
    sol = 0
    for i in range(n):
        line = lines[i]
        current_number = ""
        number_is_safe = False
        last_is_safe = False
        for j in range(m+1):
            if j == m:
                if current_number != "" and number_is_safe:
                    sol += int(current_number)
                    print("added number ", current_number)
                continue
            char = line[j]
            is_safe = get_is_safe(i, j)
            if char.isnumeric():
                current_number += char
                if is_safe or last_is_safe:
                    number_is_safe = True
            else:
                if current_number != "":
                    if is_safe:
                        number_is_safe = True
                    if number_is_safe:
                        sol += int(current_number)
                        print("added number ", current_number)
                current_number = ""
                number_is_safe = False
            last_is_safe = is_safe
    return sol

def is_symbol(c):
    return not c.isnumeric() and c != "."

def part2():
    def get_number(i, j):
        line = lines[i]
        number = ""
        j1 = j
        while j1 >= 0 and line[j1].isnumeric():
            number = line[j1] + number
            line[j1] = "."
            j1 -= 1
        j1 = j
        if number != "":
            j1 = j+1
        while j1 < m and line[j1].isnumeric():
            number = number + line[j1]
            line[j1] = "."
            j1 += 1
        return int(number) if number else 0

    with open("advent_of_code/2023/day3/in.txt") as f:
        lines = f.readlines()
    lines = [ [c for c in line.strip()] for line in lines ]
    n, m = len(lines), len(lines[0])
    sol = 0
    for i in range(n):
        line = lines[i]
        lines[i] = line
        for j in range(m):
            char = line[j]
            results = []
            if char == "*":
                for a, b in ((i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)):
                    num = get_number(a, b)
                    if num != 0:
                        results.append(num)
            if len(results) == 2:
                sol += results[0]*results[1]
    return sol


print(part2())