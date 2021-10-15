"""
Leetcode 10

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        Ls, Lp = len(s), len(p)
        dp = [[False]*(Lp+1) for _ in range(Ls+1)]
        dp[0][0] = True
        for i in range(1, Lp+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1, Ls+1):
            for j in range(1, Lp+1):
                if p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or p[j-2] in {s[i-1], '.'} and dp[i-1][j]
        return dp[-1][-1]
