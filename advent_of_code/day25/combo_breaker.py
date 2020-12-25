class ComboBreaker:
    def __init__(self):
        self.cpk, self.dpk = None, None

    def read_keys(self):
        if not self.cpk or not self.dpk:
            with open('./advent_of_code/day25/keys.txt') as reader:
                self.cpk, self.dpk = ( int(line.strip()) for line in reader.readlines() )
            return self.cpk, self.dpk

    def get_loops(self, pk, s=7):
        cur = 1
        i = 0
        while cur != pk and (i := i+1):
            cur = cur*s%20201227
        return i

    def get_key(self, s, size):
        cur = 1
        for _ in range(size):
            cur = cur*s%20201227
        return cur

    def part1(self):
        cpk, dpk = self.read_keys()
        self.cl, self.dl = self.get_loops(cpk), self.get_loops(dpk)
        return self.get_key(dpk, self.cl)
