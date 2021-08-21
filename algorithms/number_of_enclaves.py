"""
Leetcode 1020

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            self.mark(grid, i, 0)
            self.mark(grid, i, n-1)
        for j in range(1, n-1):
            self.mark(grid, 0, j)
            self.mark(grid, m-1, j)
        return sum(sum(row) for row in grid)

    def mark(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        in_board = 0 <= i < m and 0 <= j < n
        if not in_board or grid[i][j] == 0:
            return
        grid[i][j] = 0
        for i1, j1 in self.DIRS:
            self.mark(grid, i+i1, j+j1)
