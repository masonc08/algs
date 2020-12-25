import collections


class LobbyLayout:
    def __init__(self):
        self.instructions = []
        self.floor = None

    def read_instructions(self):
        if not self.instructions:
            with open('./advent_of_code/day24/instructions.txt') as reader:
                self.instructions = [ line.strip() for line in reader.readlines() ]
        return self.instructions

    DIRS = {
        "se": (0, -1, 1),
        "sw": (-1, 0, 1),
        "nw": (0, 1, -1),
        "ne": (1, 0, -1),
        "w": (-1, 1, 0),
        "e": (1, -1, 0)
    }

    def part1(self):
        instructions = self.read_instructions()
        blacks = 0
        locs = collections.defaultdict(int)
        for instruction in instructions:
            i, L = 0, len(instruction)
            x = y = z = 0
            while i < L:
                duo = instruction[i:i+2]
                single = instruction[i]
                if i != L-1 and duo in self.DIRS:
                    x1, y1, z1 = self.DIRS[duo]
                    x, y, z = x+x1, y+y1, z+z1
                    i += 2
                elif single in self.DIRS:
                    x1, y1, z1 = self.DIRS[single]
                    x, y, z = x+x1, y+y1, z+z1
                    i += 1
                else:
                    raise Exception("Incorrect parsing")
            locs[(x, y, z)] ^= 1
            if locs[(x, y, z)] == 0:
                blacks -= 1
            else:
                blacks += 1
        self.floor = locs
        return blacks

    def get_bounds(self):
        a, b, c = ( [float('inf'), float('-inf')] for _ in range(3) )
        for x, y, z in self.floor:
            if self.floor[(x, y, z)] == 1:
                a[0], b[0], c[0] = min(x, a[0]), min(y, b[0]), min(z, c[0])
                a[1], b[1], c[1] = max(x, a[1]), max(y, b[1]), max(z, c[1])
        return a, b, c

    def increment(self, a, b, c):
        a[0], b[0], c[0] = a[0]-1, b[0]-1, c[0]-1
        a[1], b[1], c[1] = a[1]+1, b[1]+1, c[1]+1

    def get_blacks(self, x, y, z, flr):
        return sum(flr[(x+x1, y+y1, z+z1)] for x1, y1, z1 in self.DIRS.values())

    def part2(self):
        self.part1()
        a, b, c = self.get_bounds()
        flr = self.floor
        for i in range(100):
            self.increment(a, b, c)
            a1, b1, c1 = ( [float('inf'), float('-inf')] for _ in range(3) )
            new_flr = collections.defaultdict(int)
            for x in range(a[0], a[1]+1):
                for y in range(b[0], b[1]+1):
                    for z in range(c[0], c[1]+1):
                        blacks = self.get_blacks(x, y, z, flr)
                        if flr[(x, y, z)] == 0 and blacks == 2 or \
                            flr[(x, y, z)] == 1 and blacks != 0 and blacks <= 2:
                            new_flr[(x, y, z)] = 1
                            a1[0], b1[0], c1[0] = min(x, a1[0]), min(y, b1[0]), min(z, c1[0])
                            a1[1], b1[1], c1[1] = max(x, a1[1]), max(y, b1[1]), max(z, c1[1])
            a, b, c, flr = a1, b1, c1, new_flr
        return len(new_flr)
