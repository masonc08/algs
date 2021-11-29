class EncodingError:
    def __init__(self):
        self.lines = None
        self.invalid = None


    def get_lines(self):
        if not self.lines:
            with open('./advent_of_code/day09/encryption.txt') as reader:
                lines = reader.readlines()
            self.lines = [ int(line.strip()) for line in lines ]
        return self.lines

    def part1(self):
        if not self.invalid:
            lines = self.get_lines()
            for i in range(25, len(lines)):
                tar = lines[i]
                cnt = set()
                found = False
                for j in range(i-25, i):
                    a = lines[j]
                    if tar-a in cnt:
                        found = True
                        break
                    cnt.add(a)
                if not found:
                    self.invalid = tar
                    return self.invalid
            raise Exception("All numbers have a pair")
        return self.invalid

    def part2(self):
        lines = self.get_lines()
        invalid = self.part1()
        pfx = {}
        cur = 0
        a, b = 0, 0
        for i, n in enumerate(lines):
            if cur-invalid in pfx:
                a = pfx[cur-invalid]
                b = i-1
                break
            pfx[cur] = i
            cur += n
        lo, hi = 0x7fffffff, -0x80000000
        for i in range(a, b+1):
            lo = min(lo, lines[i])
            hi = max(hi, lines[i])
        return lo+hi
