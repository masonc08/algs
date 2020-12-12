class RainRisk:
    def __init__(self):
        self.directions = None

    def read_directions(self):
        if self.directions is None:
            with open('./advent_of_code/day12/directions.txt') as reader:
                self.directions = [ (s[0], int(s[1:])) for s in reader.readlines() ]
        return self.directions
    
    def part1(self):
        directions = self.read_directions()
        cur = 0
        dirs = ['E', 'N', 'W', 'S']
        ttl = {
            'E': 0,
            'N': 0,
            'W': 0,
            'S': 0
        }
        for vect, scal in directions:
            if vect in ['L', 'R']:
                cur += (scal if vect == 'L' else -scal)
                cur = (cur+360)%360
            elif vect == 'F':
                ttl[dirs[cur//90]] += scal
            elif vect in ['N', 'S', 'E', 'W']:
                ttl[vect] += scal
            else:
                raise Exception("Unexpected input", vect, scal)
        print(ttl)
        return abs(ttl['E']-ttl['W']) + abs(ttl['N']-ttl['S'])

    def part2(self):
        directions = self.read_directions()
        n, e = 1, 10
        tn, te = 0, 0
        for vect, scal in directions:
            if vect in ['L', 'R']:
                if vect == 'R':
                    scal = -scal
                    scal = (scal+360)%360
                conversions = [lambda n, e: (n, e), lambda n, e: (e, -n), lambda n, e: (-n, -e), lambda n, e: (-e, n)]
                n, e = conversions[scal//90](n, e)
            elif vect == 'F':
                tn += (n*scal)
                te += (e*scal)
            elif vect in ['N', 'S']:
                n += (scal if vect == 'N' else -scal)
            elif vect in ['W', 'E']:
                e += (scal if vect == 'E' else -scal)
            else:
                raise Exception("Unexpected input", vect, scal)
        return abs(tn)+abs(te)
