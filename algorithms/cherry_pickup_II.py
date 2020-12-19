"""
Leetcode 1493
December Leetcoding Challenge
Runtime: 1128 ms, faster than 57.42% of Python3 online submissions for Cherry Pickup II.
Memory Usage: 43.4 MB, less than 8.60% of Python3 online submissions for Cherry Pickup II.
"""


import functools


class Solution:
    DIRS = tuple(range(-1, 2))
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        @functools.lru_cache(maxsize=None)
        def dfs(d, a, b):
            if d == m:
                return 0
            cur = grid[d][a] if a == b else grid[d][a]+grid[d][b]
            best = 0
            for a1 in self.DIRS:
                for b1 in self.DIRS:
                    if 0 <= a+a1 < n and 0 <= b+b1 < n:
                        best = max(best, dfs(d+1, a+a1, b+b1))
            return cur+best

        return dfs(0, 0, n-1)
