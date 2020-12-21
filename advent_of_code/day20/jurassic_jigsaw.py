from JigsawPiece import JigsawPiece
from collections import defaultdict, Counter


class JurassicJigsaw:
    def __init__(self):
        self.pieces = {}
        self.sides = defaultdict(list)

    def read_jigsaw(self):
        with open('./advent_of_code/day20/jigsaw_puzzle.txt') as reader:
            segments = reader.read().split('\n\n')
        for segment in segments:
            segment = segment.split('\n')
            n = int(segment[0].split()[1][:-1])
            puzzle_piece = segment[1:]
            piece = JigsawPiece(n, puzzle_piece)
            sides = [ piece.top for _ in piece.rotate() ]
            for side in sides:
                self.sides[side].append(n)
            self.pieces[n] = piece

    def part1(self):
        self.read_jigsaw()
        m = n = int(len(self.pieces)**(1/2))
        sol = [[None]*m for _ in range(n)]
        ct = Counter()
        for key in self.sides:
            if len(self.sides[key]) == 1:
                ct[self.sides[key][0]] += 1
        edge = None
        for key in ct:
            if ct[key] == 4:
                edge = key
        edge = self.pieces[edge]
        for _ in edge.rotate():
            if len(self.sides[edge.top]) == 1 and len(self.sides[edge.left]) == 1:
                break
        sol[0][0] = edge
        edge.used = True
        for i in range(len(sol)):
            for j in range(len(sol[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    left = sol[i][j-1]
                    for cand_id in self.sides[left.right]:
                        cand = self.pieces[cand_id]
                        if not cand.used:
                            for _ in cand.rotate():
                                if (cand.left == left.right or cand.left[::-1] == left.right) and len(self.sides[cand.top]) == 1:
                                    break
                            sol[i][j] = cand
                            cand.used = True
                            break
                elif j == 0:
                    top = sol[i-1][j]
                    for cand_id in self.sides[top.bottom]:
                        cand = self.pieces[cand_id]
                        if not cand.used:
                            for _ in cand.rotate():
                                if (cand.top == top.bottom or cand.top[::-1] == top.bottom) and len(self.sides[cand.left]) == 1:
                                    break
                            sol[i][j] = cand
                            cand.used = True
                            break
                else:
                    left = sol[i][j-1]
                    top = sol[i-1][j]
                    for cand_id in self.sides[left.right]:
                        cand = self.pieces[cand_id]
                        if not cand.used:
                            for _ in cand.rotate():
                                if (cand.left == left.right or cand.left[::-1] == left.right) and (cand.top == top.bottom or cand.top[::-1] == top.bottom):
                                    break
                            sol[i][j] = cand
                            cand.used = True
                            break
        self.part1sol = sol
        return sol[0][0].tile_num*sol[-1][0].tile_num*sol[-1][-1].tile_num*sol[0][-1].tile_num

    LOCS = (
        (0, 0),
        (1, 1),
        (1, 4),
        (0, 5),
        (0, 6),
        (1, 7),
        (1, 10),
        (0, 11),
        (0, 12),
        (1, 13),
        (1, 16),
        (0, 17),
        (0, 18),
        (-1, 18),
        (0, 19)
    )

    def is_monster(self, i, j, board, visited):
        for i1, j1 in self.LOCS:
            if i+i1 < 0 or i+i1 >= len(board) or j+j1 < 0 or j+j1 >= len(board) or board[i+i1][j+j1] != '#':
                return set()
            visited.add((i+i1, j+j1))
        return visited
        

    def part2(self):
        self.part1()
        t = self.part1sol
        picture = []
        for i in range(len(t)):
            for j in range(1, len(t[i][0].pattern)-1):
                line = []
                for k in range(len(t[0])):
                    for m in range(1, len(t[i][k].pattern[j])-1):
                        c = t[i][k].pattern[j][m]
                        line.append(c)
                picture.append(''.join(line))
        puzzle = JigsawPiece(None, picture)
        monsters = set()
        for _ in puzzle.rotate():
            board = puzzle.pattern
            for i in range(len(board)):
                for j in range(len(board[0])):
                    monsters = monsters | self.is_monster(i, j, board, set())
            if len(monsters) != 0:
                break
        ct = sum(line.count('#') for line in puzzle.pattern)
        return ct-len(monsters)

print(JurassicJigsaw().part2())


    # def call_next(self, i, j, sol):
    #     if j == len(sol[0])-1:
    #         if self.can_make(i+1, 0, sol):
    #             return True
    #     else:
    #         if self.can_make(i, j+1, sol):
    #             return True
    #     return False

    # def can_make(self, i, j, sol):
    #     if i == len(sol) or j == len(sol[0]):
    #         return True
    #     if (i == 0) ^ (j == 0):
    #         neib_id = sol[i][j-1] if i == 0 else sol[i-1][j]
    #         neib_piece = self.pieces[neib_id]
    #         pattern = neib_piece.right if i == 0 else neib_piece.bottom
    #         for cand_id in self.sides[pattern]:
    #             cand = self.pieces[cand_id]
    #             if not cand.used:
    #                 sol[i][j] = cand_id
    #                 cand.used = True
    #                 match = (cand.left == neib_piece.right) if i == 0 \
    #                     else (cand.top == neib_piece.bottom)
    #                 for _ in cand.rotate():
    #                     if match and self.call_next(i, j, sol):
    #                         return True
    #                 sol[i][j] = None
    #                 cand.used = False
    #     elif i != 0 and j != 0:
    #         top_id = sol[i-1][j]
    #         top_piece = self.pieces[top_id]
    #         left_id = sol[i][j-1]
    #         left_piece = self.pieces[left_id]
    #         pattern = left_piece.right
    #         for cand_id in self.sides[pattern]:
    #             cand = self.pieces[cand_id]
    #             if not cand.used:
    #                 sol[i][j] = cand_id
    #                 cand.used = True
    #                 match = cand.left == left_piece.right and cand.top == top_piece.bottom
    #                 for _ in cand.rotate():
    #                     if match and self.call_next(i, j, sol):
    #                         return True
    #                 sol[i][j] = None
    #                 cand.used = False
    #     else:
    #         raise Exception("Logic error")
    #     return False

    # def part1(self):
    #     self.read_jigsaw()
    #     m = n = int(len(self.pieces)**(1/2))
    #     sol = [[None]*m for _ in range(n)]
    #     for piece_num in self.pieces:
    #         piece = self.pieces[piece_num]
    #         sol[0][0] = piece_num
    #         piece.used = True
    #         for _ in range(4):
    #             if self.can_make(0, 1, sol):
    #                 return sol[0][0]*sol[0][-1]*sol[-1][0]*sol[-1][-1]
    #             piece.rotate()
    #         piece.used = False
    #     raise Exception("No solution")