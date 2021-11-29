import collections


class SeatingSystem:
    dirs = {
        "nw": (-1, -1),
        "n": (-1, 0),
        "ne": (-1, 1),
        "w": (0, -1),
        "e": (0, 1),
        "sw": (1, -1),
        "s": (1, 0),
        "se": (1, 1)
    }
    def __init__(self):
        self.seats = None


    def read_lines(self):
        if self.seats is None:
            with open('./advent_of_code/day11/seats.txt') as reader:
                lines = reader.readlines()
            self.seats = [ line.strip() for line in lines ]
        return self.seats


    def count(self, seats, i, j):
        adj_seats = [ seats[i+i1][j+j1] for i1, j1 in self.dirs.values() if (0 <= (i+i1) < len(seats) and 0 <= (j+j1) < len(seats[0])) ]
        return collections.Counter(adj_seats)


    def part1(self):
        prev = self.read_lines()
        same, occupied = False, 0
        while not same:
            cur = [[None]*len(prev[0]) for _ in prev]
            same, occupied = True, 0
            for i, row in enumerate(prev):
                for j, cell in enumerate(row):
                    count = self.count(prev, i, j)
                    if cell == 'L' and count['#'] == 0:
                        cur[i][j] = '#'
                    elif cell == '#' and count['#'] >= 4:
                        cur[i][j] = 'L'
                    else:
                        cur[i][j] = prev[i][j]
                    if cur[i][j] == '#':
                        occupied += 1
                    if cur[i][j] != prev[i][j]:
                        same = False
            prev = cur
        return occupied


    def fetch(self, key, cache, seats, i, j):
        if (not 0 <= i < len(seats)) or (not 0 <= j < len(seats[0])):
            return None
        if seats[i][j] != '.':
            return seats[i][j]
        if key in cache[(i, j)]:
            return cache[(i, j)][key]
        x = self.fetch(key, cache, seats, i+self.dirs[key][0], j+self.dirs[key][1])
        if x is not None:
            cache[(i, j)][key] = x
        return x


    def count_vision(self, seats, cache, i, j):
        vision = cache[(i, j)]
        for key in self.dirs:
            i1, j1 = self.dirs[key]
            x = self.fetch(key, cache, seats, i+i1, j+j1)
            if x is not None:
                vision[key] = x
        cache[(i, j)] = vision
        return collections.Counter(vision.values())



    def part2(self):
        prev = self.read_lines()
        same, occupied = False, 0
        while not same:
            cur = [[None]*len(prev[0]) for _ in prev]
            cache = collections.defaultdict(dict)
            same, occupied = True, 0
            for i, row in enumerate(prev):
                for j, cell in enumerate(row):
                    if cell == '.':
                        cur[i][j] = prev[i][j]
                    else:
                        count = self.count_vision(prev, cache, i, j)
                        if cell == 'L' and count['#'] == 0:
                            cur[i][j] = '#'
                        elif cell == '#' and count['#'] >= 5:
                            cur[i][j] = 'L'
                        else:
                            cur[i][j] = prev[i][j]
                        if cur[i][j] == '#':
                            occupied += 1
                        if cur[i][j] != prev[i][j]:
                            same = False
            prev = cur
        return occupied
