"""
Leetcode 1015
"""


import math


class Solution:
    """
    Runtime: 40 ms, faster than 94.64% of Python3 online submissions for Smallest Integer Divisible by K.
    Memory Usage: 14 MB, less than 85.71% of Python3 online submissions for Smallest Integer Divisible by K.
    """
    def smallestRepunitDivByK(self, K: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        sol = 0
        for i in range(1, K+1):
            sol = (sol*10+1)%K
            if sol == 0:
                return i
        return -1


    """
    Runtime: 2012 ms, faster than 23.81% of Python3 online submissions for Smallest Integer Divisible by K.
    Memory Usage: 18.3 MB, less than 7.74% of Python3 online submissions for Smallest Integer Divisible by K.
    """
    # def smallestRepunitDivByK(self, K: int) -> int:
    #     sol = int(math.log10(K))+1
    #     x = 0
    #     for _ in range(sol):
    #         x *= 10
    #         x += 1
    #     if K > x:
    #         x *= 10
    #         x += 1
    #         sol += 1
    #     seen = set()
    #     cur = x%K
    #     while cur not in seen:
    #         if cur == 0:
    #             return sol
    #         seen.add(cur)
    #         x *= 10
    #         x += 1
    #         cur = x%K
    #         sol += 1
    #     return -1
