class ReportRepair:
    def get_lines(self):
        with open('./advent_of_code/day03/toboggan_hill.txt') as reader:
            lines = reader.readlines()
        return [ line.strip() for line in lines ]


    wrap = lambda x, lim: (x+lim)%lim


    def part1(self, r, d):
        hill = self.get_lines()
        sol = 0
        x = 0
        for i in range(0, len(hill), d):
            y = hill[i]
            if y[x] == "#":
                sol += 1
            x += r
            x %= len(y)
        return sol


    def part2(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        sol = 1
        for slope in slopes:
            sol *= self.part1(*slope)
        return sol



print(ReportRepair().part2())
