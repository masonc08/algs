import collections


class ConwayCubes:

    def __init__(self):
        self.grid = None

    def read_seed(self, part2=False):
        if self.grid is None:
            with open('./advent_of_code/day17/seed.txt') as reader:
                lines = [ line.strip() for line in reader.readlines()]
            self.grid = [[[['.']*(13+len(lines[0])) for _ in range(13+len(lines))] for _ in range(13)] for _ in range(13)] if part2 else \
                [[['.']*(13+len(lines[0])) for _ in range(13+len(lines))] for _ in range(13)]
            for i, line in enumerate(lines):
                for j, c in enumerate(line):
                    if part2:
                        self.grid[6][6][i+6][j+6] = c
                    else:
                        self.grid[6][i+6][j+6] = c
        return self.grid

    def in_bounds(self, k, i, j, m=None):
        if m is None:
            return 0 <= k < len(self.grid) and \
                0 <= i < len(self.grid[0]) and \
                0 <= j < len(self.grid[0][0])
        return 0 <= m < len(self.grid) and \
            0 <= k < len(self.grid[0]) and \
            0 <= i < len(self.grid[0][0]) and \
            0 <= j < len(self.grid[0][0][0])

    def get_nbrs(self, k, i, j, m=None):
        pos = (-1, 0, 1)
        for k1 in pos:
            for i1 in pos:
                for j1 in pos:
                    if m is None:
                        if k1 == i1 == j1 == 0 or not self.in_bounds(k+k1, i+i1, j+j1):
                            continue
                        yield k+k1, i+i1, j+j1
                    for m1 in pos:
                        if k1 == i1 == j1 == m1 == 0 or not self.in_bounds(k+k1, i+i1, j+j1, m+m1):
                            continue
                        yield m+m1, k+k1, i+i1, j+j1
                

    def part1(self):
        self.read_seed()
        for _ in range(6):
            new = [[['.']*len(self.grid[0][0]) for _ in self.grid[0]] for _ in self.grid]
            for k in range(len(self.grid)):
                for i in range(len(self.grid[0])):
                    for j in range(len(self.grid[0][0])):
                        ct = collections.Counter([self.grid[a][b][c] for a, b, c in self.get_nbrs(k, i, j)])
                        if self.grid[k][i][j] == '#' and ct['#'] not in {2, 3}:
                            new[k][i][j] = '.'
                        elif self.grid[k][i][j] == '.' and ct['#'] in {3}:
                            new[k][i][j] = '#'
                        else:
                            new[k][i][j] = self.grid[k][i][j]
            self.grid = new
        sol = 0
        for k in range(len(self.grid)):
            for i in range(len(self.grid[0])):
                for j in range(len(self.grid[0][0])):
                    if self.grid[k][i][j] == '#':
                        sol += 1
        return sol

    def part2(self):
        self.read_seed(part2=True)
        for _ in range(6):
            new = [[[['.']*len(self.grid[0][0][0]) for _ in self.grid[0][0]] for _ in self.grid[0]] for _ in self.grid]
            for m in range(len(self.grid)):
                for k in range(len(self.grid[0])):
                    for i in range(len(self.grid[0][0])):
                        for j in range(len(self.grid[0][0][0])):
                            ct = collections.Counter([self.grid[a][b][c][d] for a, b, c, d in self.get_nbrs(k, i, j, m)])
                            if self.grid[m][k][i][j] == '#' and ct['#'] not in {2, 3}:
                                new[m][k][i][j] = '.'
                            elif self.grid[m][k][i][j] == '.' and ct['#'] in {3}:
                                new[m][k][i][j] = '#'
                            else:
                                new[m][k][i][j] = self.grid[m][k][i][j]
            self.grid = new
        sol = 0
        for m in range(len(self.grid)):
            for k in range(len(self.grid[0])):
                for i in range(len(self.grid[0][0])):
                    for j in range(len(self.grid[0][0][0])):
                        if self.grid[m][k][i][j] == '#':
                            sol += 1
        return sol
