"""
Leetcode 808
Runtime: 32 ms, faster than 88.78% of Python3 online submissions for Soup Servings.
Memory Usage: 15.4 MB, less than 21.43% of Python3 online submissions for Soup Servings.
"""


import functools
import math


class Solution:
    def soupServings(self, N: int) -> float:
        @functools.lru_cache(None)
        def search(a, b):
            if a <= 0 and b <= 0:
                return 0, 1
            if a <= 0:
                return 1, 0
            if b <= 0:
                return 0, 0
            sols = [
                search(a-100, b),
                search(a-75, b-25),
                search(a-50, b-50),
                search(a-25, b-75)
            ]
            return sum(a for a, _ in sols)/4, sum(b for _, b in sols)/4
        if N > 4800:
            return 1
        a, b = search(N, N)
        return a+b/2
