"""
Leetcode 1140
Runtime: 164 ms, faster than 89.62% of Python3 online submissions for Stone Game II.
Memory Usage: 16.2 MB, less than 30.58% of Python3 online submissions for Stone Game II.
"""


import functools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        L = len(piles)
        for i in range(L-2, -1, -1):
            piles[i] += piles[i+1]

        @functools.lru_cache(None)
        def solve(s, M):
            if s+2*M >= L:
                return piles[s]
            return piles[s]-min(solve(s+i, max(i, M)) for i in range(1, 2*M+1))
        return solve(0, 1)
