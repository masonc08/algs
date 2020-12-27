"""
Leetcode 130
Runtime: 136 ms, faster than 69.15% of Python3 online submissions for Surrounded Regions.
Memory Usage: 16.3 MB, less than 35.76% of Python3 online submissions for Surrounded Regions.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def edge(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                for i1, j1 in {(0, 1), (0, -1), (-1, 0), (1, 0)}:
                    edge(i+i1, j+j1)

        for i in range(max(m, n)):
            if i < m:
                edge(i, 0), edge(i, n-1)
            if i < n:
                edge(0, i), edge(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        
