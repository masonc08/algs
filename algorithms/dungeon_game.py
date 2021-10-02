"""
Leetcode 174
October Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [-math.inf]*m
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    dp[j] = max(-dungeon[i][j], 0)+1
                else:
                    dp[j] = min(
                        max(dp[j+1]-dungeon[i][j], 1) if j < m-1 else math.inf,
                        max(dp[j]-dungeon[i][j], 1) if i < n-1 else math.inf,
                    )
        return dp[0]
