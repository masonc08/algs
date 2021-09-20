"""
Leetcode 1275
September Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col, diags, turn = [0]*3, [0]*3, [0]*2, 1
        for x, y in moves:
            row[x] += turn
            col[y] += turn
            if x == y:
                diags[0] += turn
            if x == 2-y:
                diags[1] += turn
            if any(abs(streak) == 3 for streak in (row[x], col[y], diags[0], diags[1])):
                return 'A' if turn == 1 else 'B'
            turn = -turn
        return 'Pending' if len(moves) < 9 else "Draw"
