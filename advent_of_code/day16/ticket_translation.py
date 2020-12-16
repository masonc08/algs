import collections


class TicketTranslation:
    def __init__(self):
        self.data = None

    def read_lines(self):
        with open('./advent_of_code/day16/ids.txt') as reader:
            lines = reader.read()
        self.data = [ line.split('\n') for line in lines.split('\n\n') ]
        return self.data

    def remove_invalid(self, tickets):
        sol = 0
        li = list(tickets)
        for line in li:
            rem = False
            for val in line.split(','):
                if val != '':
                    val = int(val)
                    if not any([ lo <= val <= hi for lo, hi in self.ranges ]):
                        sol += val
                        rem = True
            if rem:
                tickets.remove(line)
        return sol

    def part1(self):
        data = self.read_lines()
        self.ranges = {}
        for line in data[0]:
            name, line = line.split(': ')
            line = line.split(' or ')
            for interval in line:
                l, h = interval.split('-')
                self.ranges[(int(l), int(h))] = name
        self.nearby_tickets = set(data[-1][1:])
        return self.remove_invalid(self.nearby_tickets)

    def part2(self):
        self.part1()
        data = self.read_lines()
        nearby_tickets = [ line.split(',') for line in self.nearby_tickets if line != '' ]
        poss = collections.defaultdict(list)
        for j in range(len(nearby_tickets[0])):
            ct = collections.defaultdict(int)
            for i in range(len(nearby_tickets)):
                for l, h in self.ranges:
                    n = int(nearby_tickets[i][j])
                    if l <= n <= h:
                        ct[self.ranges[(l, h)]] += 1
            for key in ct:
                if ct[key] == len(nearby_tickets):
                    poss[key].append(j)
        kv = [ (poss[k], k) for k in poss ]
        kv.sort(key=lambda x: len(x[0]))
        used = set()
        mp = {}
        for cands, name in kv:
            new = []
            for cand in cands:
                if cand not in used:
                    new.append(cand)
            if len(new) != 1:
                raise Exception()
            mp[name] = new[0]
            used.add(new[0])
        tickets = data[1][1].split(',')
        sol = 1
        for key in mp:
            if "departure" in key:
                sol *= int(tickets[mp[key]])
        return sol
            