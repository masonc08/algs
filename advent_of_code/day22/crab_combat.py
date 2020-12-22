import collections
import itertools


class CrabCombat:
    def __init__(self):
        self.p1 = None
        self.p2 = None

    def read_cards(self):
        if not self.p1 or not self.p1:
            with open('./advent_of_code/day22/cards.txt') as reader:
                lines = reader.read().split('\n\n')
            cards = [ int(num) for num in lines[0].split('\n')[1:] ]
            self.p1 = collections.deque(cards)
            cards = [ int(num) for num in lines[1].split('\n')[1:] ]
            self.p2 = collections.deque(cards)
        return self.p1.copy(), self.p2.copy()

    def get_score(self, p1, p2):
        winner = p1 or p2
        sol = i = 0
        while (i := i+1) and winner:
            sol += i*winner.pop()
        return sol

    def part1(self):
        p1, p2 = self.read_cards()
        while p1 and p2:
            a, b = p1.popleft(), p2.popleft()
            if a > b:
                p1 += a, b
            else:
                p2 += b, a
        return self.get_score(p1, p2)

    def part2(self):
        p1, p2 = self.read_cards()
        def play(p1, p2):
            seen = set()
            while p1 and p2:
                t1, t2 = tuple(p1), tuple(p2)
                if t1 in seen or t2 in seen:
                    while p2:
                        p2.pop()
                    return
                seen.add(t1), seen.add(t2)
                a, b = p1.popleft(), p2.popleft()
                if a <= len(p1) and b <= len(p2):
                    p1c = collections.deque(itertools.islice(p1, 0, a))
                    p2c = collections.deque(itertools.islice(p2, 0, b))
                    play(p1c, p2c)
                    if not p1c:
                        p2 += b, a
                    else:
                        p1 += a, b
                else:
                    if a > b:
                        p1 += a, b
                    else:
                        p2 += b, a

        play(p1, p2)
        return self.get_score(p1, p2)
