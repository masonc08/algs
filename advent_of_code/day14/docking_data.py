class DockingData:
    def __init__(self):
        self.lines = None

    def get_lines(self):
        if not self.lines:
            with open('./advent_of_code/day14/docking_program.txt') as reader:
                lines = reader.readlines()
            self.lines = [ line.strip() for line in lines ]
        return self.lines

    def part1(self):
        lines = self.get_lines()
        mask = ''
        vals = {}
        for line in lines:
            if line[:4] == "mask":
                mask = line.split(" = ")[1]
            else:
                l, r = line.index("["), line.index("]")
                key = int(line[l+1:r])
                num = int(line.split(" = ")[1])
                for i in range(len(mask)):
                    c = mask[-i-1]
                    if c == '1':
                        num |= (1<<i)
                    elif c == '0':
                        num &= ~(1<<i)
                if num != 0:
                    vals[key] = num
        return sum(vals.values())


    def set_all_permutations(self, mp, li, key, num, d=0):
        if num != 0:
            mp[key] = num
        if d >= len(li):
            return
        self.set_all_permutations(mp, li, key, num, d+1)
        self.set_all_permutations(mp, li, key^(1<<li[d]), num, d+1)


    def part2(self):
        lines = self.get_lines()
        mask = ''
        vals = {}
        for line in lines:
            if line[:4] == "mask":
                mask = line.split(" = ")[1]
            else:
                l, r = line.index("["), line.index("]")
                key = int(line[l+1:r])
                num = int(line.split(" = ")[1])
                floats = []
                for i in range(len(mask)):
                    c = mask[-i-1]
                    if c == '1':
                        key |= (1<<i)
                    elif c == 'X':
                        floats.append(i)
                self.set_all_permutations(vals, floats, key, num)
        return sum(vals.values())
                

print(DockingData().part2())
