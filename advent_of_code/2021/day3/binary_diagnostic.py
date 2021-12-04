def part1():
    ct = [0]*12
    with open('binary_diagnostic.txt') as r:
        for line in r:
            line = line.strip()
            for i, c in enumerate(line):
                if c == '0':
                    ct[i] -= 1
                else:
                    ct[i] += 1
    gamma = epsilon = 0
    for v in ct:
        gamma <<= 1
        epsilon <<= 1
        if v > 0:
            gamma |= 1
        else:
            epsilon |= 1
    return gamma*epsilon

def part2():
    with open('binary_diagnostic.txt') as r:
        M = set(line.strip() for line in r.readlines())
    for j in range(12):
        zeros, ones = set(), set()
        for line in M:
            if line[j] == '0':
                zeros.add(line)
            else:
                ones.add(line)
        if len(ones) >= len(zeros):
            M = ones
        else:
            M = zeros
        if len(M) == 1:
            break
    A = list(M)[0]
    with open('binary_diagnostic.txt') as r:
        M = set(line.strip() for line in r.readlines())
    for j in range(12):
        zeros, ones = set(), set()
        for line in M:
            if line[j] == '0':
                zeros.add(line)
            else:
                ones.add(line)
        if len(ones) >= len(zeros):
            M = zeros
        else:
            M = ones
        if len(M) == 1:
            break
    B = list(M)[0]
    return int(A, 2)*int(B, 2)

print(part2())
