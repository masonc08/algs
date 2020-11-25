"""
Leetcode 1015
Runtime: 2012 ms, faster than 23.81% of Python3 online submissions for Smallest Integer Divisible by K.
Memory Usage: 18.3 MB, less than 7.74% of Python3 online submissions for Smallest Integer Divisible by K.
"""


import math


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        sol = int(math.log10(K))+1
        x = 0
        for _ in range(sol):
            x *= 10
            x += 1
        if K > x:
            x *= 10
            x += 1
            sol += 1
        seen = set()
        cur = x%K
        while cur not in seen:
            if cur == 0:
                return sol
            seen.add(cur)
            x *= 10
            x += 1
            cur = x%K
            sol += 1
        return -1
