"""
Leetcode 994
Runtime: 52 ms, faster than 63.79% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14.2 MB, less than 52.53% of Python3 online submissions for Rotting Oranges.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stk = []
        fresh = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    stk += (i, j),
                if cell == 1:
                    fresh.add((i, j))
        if not stk:
            if fresh:
                return -1
            else:
                return 0
        waves = 0
        while stk:
            new = []
            while stk:
                i, j = stk.pop()
                for i1, i2 in self.get_nbrs(i, j, grid):
                    if grid[i1][i2] == 1:
                        new += (i1, i2),
                        grid[i1][i2] = 2
                        fresh.remove((i1, i2))
            stk = new
            waves += 1
        return waves-1 if not fresh else -1

    def get_nbrs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        for i1, j1 in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
            if 0 <= i+i1 < m and 0 <= j+j1 < n:
                yield i+i1, j+j1
