class Board:
    def __init__(self, data) -> None:
        self.rows, self.cols = [5]*5, [5]*5
        self.locs = {}
        for i, row in enumerate(data):
            for j, v in enumerate(row):
                self.locs[v] = (i, j)
    
    def remove(self, n):
        if n not in self.locs:
            return None
        i, j = self.locs[n]
        del self.locs[n]
        self.rows[i] -= 1
        self.cols[j] -= 1
        if self.rows[i] == 0 or self.cols[j] == 0:
            return n*sum(self.locs)
        return None

def part1():
    with open('advent_of_code/2021/day4/giant_squid.txt') as r:
        calls = tuple(map(int, next(r).strip().split(',')))
        next(r)
        boards = []
        cur = []
        for line in r:
            if line == '\n':
                boards.append(Board(cur))
                cur = []
            else:
                cur.append(list(map(int, line.strip().split())))
    for call in calls:
        for board in boards:
            res = board.remove(call)
            if res is not None:
                return res
    raise Exception()

def part2():
    with open('advent_of_code/2021/day4/giant_squid.txt') as r:
        calls = tuple(map(int, next(r).strip().split(',')))
        next(r)
        boards = []
        cur = []
        for line in r:
            if line == '\n':
                boards.append(Board(cur))
                cur = []
            else:
                cur.append(list(map(int, line.strip().split())))
    sol = None
    for call in calls:
        new = []
        for board in boards:
            res = board.remove(call)
            if res is not None:
                sol = res
            else:
                new.append(board)
        boards = new
    return sol
        
print(part2())
