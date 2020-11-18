"""
Leetcode 858
November Leetcoding challenge
Runtime: 28 ms, faster than 76.84% of Python3 online submissions for Mirror Reflection.
Memory Usage: 14.2 MB, less than 31.23% of Python3 online submissions for Mirror Reflection.
"""


import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        p = (p//g)%2
        q = (q//g)%2
        return 1 if p and q else 0 if p else 2
