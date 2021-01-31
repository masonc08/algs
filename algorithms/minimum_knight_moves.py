"""
Leetcode 1197
O(7^(d/2)) runtime and space
Double sourced searching
Runtime: 2668 ms, faster than 46.29% of Python3 online submissions for Minimum Knight Moves.
Memory Usage: 39.6 MB, less than 41.77% of Python3 online submissions for Minimum Knight Moves.
"""


import collections


class Solution:
    MOVES = ((-2, 1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2))
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        x, y = abs(x), abs(y)
        seenA, seenB = {(0, 0): 0}, {(x, y): 0}
        qA, qB = collections.deque(((0, 0),)), collections.deque(((x, y),))
        while qA or qB:
            for q, seen, oseen in ((qA, seenA, seenB), (qB, seenB, seenA)):
                if not q:
                    continue
                i, j = q.popleft()
                wave = seen[(i, j)]
                for i1, j1 in self.MOVES:
                    new_coord = (i+i1, j+j1)
                    if new_coord not in seen:
                        seen[new_coord] = wave+1
                        if new_coord in oseen:
                            return wave+1+oseen[new_coord]
                        q.append(new_coord)
        raise Exception("No solution")
