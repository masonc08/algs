import math


class ShuttleSearch:
    def __init__(self):
        self.time = None
        self.busses = None

    def read_routes(self):
        if self.time is None or self.busses is None:
            with open('./advent_of_code/day13/routes.txt') as reader:
                lines = reader.readlines()
            self.time = int(lines[0])
            self.busses = lines[1].split(',')
        return self.time, self.busses

    def part1(self):
        sol = [float('inf'), None]
        time, busses = self.read_routes()
        for bus in busses:
            if bus == 'x':
                continue
            bus = int(bus)
            sol = min([(-time)%bus, bus], sol, key=lambda x: x[0])
        return sol[0]*sol[1]


    def part2(self):
        _, busses = self.read_routes()
        equations = [] # Storing tuples (a, b), where we require an x such that x%b=a for all tuples
        first = 0
        for i, bus in enumerate(busses):
            if bus != 'x':
                bus = int(bus)
                if len(equations) == 0:
                    first = i
                    equations.append((0, bus))
                else:
                    equations.append(((-(i-first))%bus, bus))
        prod = 1
        for _, mod in equations:
            prod *= mod
        sol = 0
        for res, mod in equations:
            cur = prod//mod
            i = 1
            while (cur*i)%mod != res:
                i += 1
            sol += (cur*i)
        sol %= prod
        return sol

