"""
Leetcode 1223
Runtime: 2328 ms, faster than 24.94% of Python3 online submissions for Dice Roll Simulation.
Memory Usage: 191 MB, less than 22.22% of Python3 online submissions for Dice Roll Simulation.
"""


import functools


class Solution:
    MOD = 10**9+7
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(reps, last, n):
            if n == 0:
                return 1
            sol = 0
            for i in range(1, 6+1):
                if i == last:
                    if reps < rollMax[i-1]:
                        sol = (sol+dfs(reps+1, i, n-1))%self.MOD
                else:
                    sol = (sol+dfs(1, i, n-1))%self.MOD
            return sol
        return dfs(0, -1, n)
