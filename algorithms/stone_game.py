"""
Leetcode 877
Runtime: 1632 ms, faster than 5.13% of Python3 online submissions for Stone Game.
Memory Usage: 57.2 MB, less than 22.42% of Python3 online submissions for Stone Game.
"""


import functools


class Solution:
    
    def stoneGame(self, piles: List[int]) -> bool:
        L = len(piles)
        old = []
        for size in range(1, L+1):
            new = []
            for i in range(L-size+1):
                v = piles[i]
                if size == 1:
                    new.append((v, 0))
                else:
                    diff_left = old[i+1][1] + v - old[i+1][0]
                    diff_right = old[i][1] + piles[i+size-1] - old[i][0]
                    if diff_left > diff_right:
                        new.append((old[i+1][1]+v, old[i+1][0]))
                    else:
                        new.append((old[i][1]+piles[i+size-1], old[i][0]))
            old = new
        return any(a > b for a, b in old)

    # def stoneGame(self, piles: List[int]) -> bool:
    #     @functools.lru_cache(None)
    #     def select(s, e):
    #         if s == e:
    #             return piles[s], 0
    #         sol = [0, 0]
    #         a, b = select(s+1, e)
    #         sol = max(sol, [b+piles[s], a], key=lambda x: x[0])
    #         a, b = select(s, e-1)
    #         sol = max(sol, [b+piles[e], a], key=lambda x: x[0])
    #         return sol
    #     a, b = select(0, len(piles)-1)
    #     return a > b
