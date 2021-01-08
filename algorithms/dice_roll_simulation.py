"""
Leetcode 1223
"""


import functools


"""
O(NMFF) runtime, O(MF) space, N=n, M=max(rollMax), F=faces on die
DP solution
Runtime: 1820 ms, faster than 35.60% of Python3 online submissions for Dice Roll Simulation.
Memory Usage: 14.4 MB, less than 95.01% of Python3 online submissions for Dice Roll Simulation.
"""
class Solution:
    MOD = 10**9+7
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0, 1] + [0]*15 for _ in range(6)]
        for _ in range(n-1):
            new = [[0]*17 for _ in range(6)]
            for i in range(6):
                for j in range(1, rollMax[i]+1):
                    for k in range(6):
                        if i == k:
                            if j < rollMax[i]:
                                new[i][j+1] = (new[i][j+1]+dp[i][j])%self.MOD
                        else:
                            new[k][1] = (new[k][1]+dp[i][j])%self.MOD
            dp = new
        return sum(map(lambda x: sum(x)%self.MOD, dp))%self.MOD


"""
O(NMFF) runtime, O(NMF) space
Recursive solution with LRU cache
Runtime: 1820 ms, faster than 35.60% of Python3 online submissions for Dice Roll Simulation.
Memory Usage: 14.4 MB, less than 95.01% of Python3 online submissions for Dice Roll Simulation.
"""
# class Solution:
#     MOD = 10**9+7
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         @functools.lru_cache(None)
#         def dfs(reps, last, n):
#             if n == 0:
#                 return 1
#             sol = 0
#             for i in range(1, 6+1):
#                 if i == last:
#                     if reps < rollMax[i-1]:
#                         sol = (sol+dfs(reps+1, i, n-1))%self.MOD
#                 else:
#                     sol = (sol+dfs(1, i, n-1))%self.MOD
#             return sol
#         return dfs(0, -1, n) 