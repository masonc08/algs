"""
Leetcode 695
Runtime: 200 ms, faster than 7.63% of Python3 online submissions for Max Area of Island.
Memory Usage: 19.8 MB, less than 5.54% of Python3 online submissions for Max Area of Island.
"""


class Solution:
    DIRS = ((0, 1), (0, -1), (-1, 0), (1, 0))
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        sol = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return sum(dfs(i+i1, j+j1) for i1, j1 in self.DIRS)+1
            return 0
        for i in range(m):
            for j in range(n):
                sol = max(dfs(i, j), sol)
        return sol
