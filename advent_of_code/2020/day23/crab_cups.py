class Cup:
    def __init__(self, n, next=None):
        self.n = n
        self.next = next


class CrabCups:
    def __init__(self):
        self.mp = {}
        self.head = None

    def read_cups(self):
        if not self.mp or not self.head:
            with open('./advent_of_code/day23/cups.txt') as reader:
                nums = [ int(num) for num in reader.read().split()[0] ]
            s = prev = Cup(-1)
            for num in nums:
                prev.next = Cup(num)
                self.mp[num] = prev.next
                prev = prev.next
            for i in range(max(nums)+1, 1000001):
                prev.next = Cup(i)
                self.mp[i] = prev.next
                prev = prev.next
            prev.next = s.next
            self.head = s.next
        return self.mp, self.head

    def get_cups(self, cup, n):
        containing = set()
        a = cup.next
        b = cup
        for _ in range(n):
            b = b.next
            containing.add(b.n)
        cup.next = b.next
        b.next = None
        return a, b, containing

    def wrap(self, n):
        n -= 1
        L = len(self.mp)
        return ((n+L)%L)+1

    def part1(self):
        cups, cur = self.read_cups()
        for _ in range(10000000):
            s, e, picked_up = self.get_cups(cur, 3)
            n = self.wrap(cur.n-1)
            while n in picked_up:
                n = self.wrap(n-1)
            dest = cups[n]
            dest.next, e.next = s, dest.next
            cur = cur.next
        return int(cups[1].next.n)*int(cups[1].next.next.n)
