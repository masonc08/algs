"""
Leetcode 44

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        Ls, Lp = len(s), len(p)
        dp = [True] + [False]*Lp
        for j, cp in enumerate(p):
            if cp == '*':
                dp[j+1] = dp[j]
        for cs in s:
            new = [False]*(Lp+1)
            for j, cp in enumerate(p):
                if cp in {cs, '?'}:
                    new[j+1] = dp[j]
                elif cp == '*':
                    new[j+1] = new[j] or dp[j+1]
            dp = new
        return dp[-1]
