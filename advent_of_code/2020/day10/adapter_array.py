import collections


class AdapterArray:
    def __init__(self):
        self.lines = None


    def get_lines(self):
        if not self.lines:
            with open('./advent_of_code/day10/joltage_differences.txt') as reader:
                lines = reader.readlines()
            self.lines = [ int(line.strip()) for line in lines ]
        return self.lines


    def part1(self):
        lines = self.get_lines()
        rem = set(lines)
        rem.add(0)
        sol = collections.defaultdict(int)
        l = r = lines[0]
        while l-1 in rem or l-2 in rem or l-3 in rem:
            if l-1 in rem:
                sol[1] += 1
                l -= 1
            elif l-2 in rem:
                sol[2] += 1
                l -= 2
            else:
                sol[3] += 1
                l -= 3
        while r+1 in rem or r+2 in rem or r+3 in rem:
            if r+1 in rem:
                sol[1] += 1
                r += 1
            elif r+2 in rem:
                sol[2] += 1
                r += 2
            else:
                sol[3] += 1
                r += 3
        return sol[1]*(sol[3]+1)


    def part2(self):
        lines = self.get_lines()
        rem = set(lines)
        dp = [0, 0, 1]
        i = 1
        while i+1 in rem or i+2 in rem or i+3 in rem:
            dp[0], dp[1], dp[2] = dp[1], dp[2], ((dp[0]+dp[1]+dp[2]) if i in rem else 0)
            i += 1
        return sum(dp)
