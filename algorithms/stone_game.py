"""
Leetcode 877
Runtime: 1632 ms, faster than 5.13% of Python3 online submissions for Stone Game.
Memory Usage: 57.2 MB, less than 22.42% of Python3 online submissions for Stone Game.
"""


import functools


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(None)
        def select(s, e):
            if s == e:
                return piles[s], 0
            sol = [0, 0]
            a, b = select(s+1, e)
            sol = max(sol, [b+piles[s], a], key=lambda x: x[0])
            a, b = select(s, e-1)
            sol = max(sol, [b+piles[e], a], key=lambda x: x[0])
            return sol
        a, b = select(0, len(piles)-1)
        return a > b
