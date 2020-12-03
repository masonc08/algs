"""
Leetcode 36
Runtime: 96 ms, faster than 59.46% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14.1 MB, less than 52.45% of Python3 online submissions for Valid Sudoku.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            exists = [False]*(len(row)+1)
            for j in range(len(row)):
                v = row[j]
                if v.isnumeric():
                    v = int(v)
                    if exists[v]:
                        return False
                    exists[v] = True
        for j in range(len(board[0])):
            exists = [False]*(len(board)+1)
            for i in range(len(board)):
                v = board[i][j]
                if v.isnumeric():
                    v = int(v)
                    if exists[v]:
                        return False
                    exists[v] = True
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                exists = [False]*10
                for i1 in range(i, i+3):
                    for j1 in range(j, j+3):
                        v = board[i1][j1]
                        if v.isnumeric():
                            v = int(v)
                            if exists[v]:
                                return False
                            exists[v] = True
        return True
