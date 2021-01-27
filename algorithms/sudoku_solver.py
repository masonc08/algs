"""
Leetcode 37
O(L^(L^2)) runtime, O(L^2) space
Runtime: 220 ms, faster than 60.88% of Python3 online submissions for Sudoku Solver.
Memory Usage: 14.7 MB, less than 12.92% of Python3 online submissions for Sudoku Solver.
"""


import collections


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, sqs = (collections.defaultdict(set) for _ in range(3))
        empty = collections.deque()
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != '.':
                    rows[i].add(v), cols[j].add(v), sqs[(i//3, j//3)].add(v)
                else:
                    empty.append((i, j))
        def dfs():
            i, j = empty.popleft()
            for cand in range(1, 10):
                cand = str(cand)
                row, col, sq = rows[i], cols[j], sqs[(i//3, j//3)]
                if cand not in row and cand not in col and cand not in sq:
                    row.add(cand), col.add(cand), sq.add(cand)
                    board[i][j] = cand
                    empty.pop()
                    if dfs():
                        return True
                    row.remove(cand), col.remove(cand), sq.remove(cand)
                    board[i][j] = '.'
                    empty.appendleft((i, j))
        dfs()