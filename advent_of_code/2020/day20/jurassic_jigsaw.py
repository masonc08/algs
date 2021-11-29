from JigsawPiece import JigsawPiece
from collections import defaultdict


class JurassicJigsaw:
    def __init__(self):
        self.pieces = {}
        self.sides = defaultdict(list)

    def read_jigsaw(self):
        if not self.pieces or not self.sides:
            with open('./advent_of_code/day20/jigsaw_puzzle.txt') as reader:
                segments = reader.read().split('\n\n')
            for segment in segments:
                segment = segment.split('\n')
                n = int(segment[0].split()[1][:-1])
                puzzle_piece = segment[1:]
                piece = JigsawPiece(n, puzzle_piece)
                sides = [ piece.transform()[0] for _ in range(8) ]
                for side in sides:
                    self.sides[side].append(n)
                self.pieces[n] = piece

    def get_edge_piece(self):
        ct = defaultdict(int)
        for key in self.sides:
            if len(self.sides[key]) == 1:
                ct[self.sides[key][0]] += 1
        edge = None
        for key in ct:
            if ct[key] == 4:
                edge = key
                break
        return self.pieces[edge]

    def is_similar(self, a, b):
        return a==b or a[::-1]==b

    def can_use(self, i, j):
        if i != 0 and j != 0:
            return lambda cur, top, other=None: self.is_similar(cur.top, top.bottom) and self.is_similar(cur.left, other.right)
        elif i == 0:
            return lambda cur, left, other=None: self.is_similar(cur.left, left.right) and len(self.sides[cur.top]) == 1
        elif j == 0:
            return lambda cur, top, other=None: self.is_similar(cur.top, top.bottom) and len(self.sides[cur.left]) == 1
        else:
            raise Exception("Logic error")

    def part1(self):
        self.read_jigsaw()
        m = n = int(len(self.pieces)**(1/2))
        sol = [[None]*m for _ in range(n)]
        edge = self.get_edge_piece()
        while len(self.sides[edge.top]) != 1 or len(self.sides[edge.left]) != 1:
            edge.transform()
        sol[0][0], edge.used = edge, True
        for i in range(len(sol)):
            for j in range(len(sol[0])):
                if i != 0 or j != 0:
                    neib = sol[i][j-1] if i == 0 else sol[i-1][j]
                    other = sol[i][j-1] if i != 0 and j != 0 else None
                    for cand_id in self.sides[neib.right if i == 0 else neib.bottom]:
                        cand = self.pieces[cand_id]
                        if not cand.used:
                            while not self.can_use(i, j)(cand, neib, other):
                                cand.transform()
                            sol[i][j], cand.used = cand, True
                            break
        self.finished_puzzle = sol
        return sol[0][0].tile_num*sol[-1][0].tile_num*sol[-1][-1].tile_num*sol[0][-1].tile_num

    LOCS = (
        (0, 0), (1, 1), (1, 4), (0, 5), (0, 6), (1, 7), (1, 10), (0, 11),
        (0, 12), (1, 13), (1, 16), (0, 17), (0, 18), (-1, 18), (0, 19)
    )

    def is_monster(self, i, j, board):
        visited = set()
        for i1, j1 in self.LOCS:
            if i+i1 < 0 or i+i1 >= len(board) or j+j1 < 0 or j+j1 >= len(board) or board[i+i1][j+j1] != '#':
                return set()
            visited.add((i+i1, j+j1))
        return visited

    def get_finished_puzzle(self):
        self.part1()
        m, n = len(self.finished_puzzle), len(self.finished_puzzle[0])
        picture = []
        for i in range(m):
            for j in range(1, self.finished_puzzle[i][0].m-1):
                line = []
                for k in range(n):
                    for m in range(1, self.finished_puzzle[i][k].n-1):
                        line += self.finished_puzzle[i][k].pattern[j][m],
                picture += ''.join(line),
        return JigsawPiece(None, picture)

    def part2(self):
        puzzle = self.get_finished_puzzle()
        monsters = set()
        i = 9
        while (i := i-1) and not monsters:
            puzzle.transform()
            for i in range(puzzle.m):
                for j in range(puzzle.n):
                    monsters.update(self.is_monster(i, j, puzzle.pattern))
        return sum(line.count('#') for line in puzzle.pattern)-len(monsters)

print(JurassicJigsaw().part2())
