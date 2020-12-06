"""
Leetcode 1680
Leetcode contest 218
Runtime: 1860 ms, faster than 14.29% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 14.2 MB, less than 71.43% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
"""


import math


class Solution:
    def concatenatedBinary(self, x: int) -> int:
        def helper(a, b):
            if a == b:
                return a
            mid = (a+b)//2
            l, r = helper(a, mid), helper(mid+1, b)
            l <<= (int(math.log2(r))+1)
            l |= r
            return l
        return helper(1, x)%(10**9+7)

    # def concatenatedBinary(self, n: int, s=1) -> int:
    #     if s == n:
    #         return s
    #     mid = (n+s)//2
    #     a, b = self.concatenatedBinary(mid, 1), self.concatenatedBinary(n, mid+1)
    #     a <<= (int(math.log2(b))+1)
    #     a |= b
    #     return a%(10**9+7)


    # def concatenatedBinary(self, n: int) -> int:
    #     sol = 0
    #     for i in range(1, n+1):
    #         size = int(math.log2(i))+1
    #         sol <<= size
    #         sol |= i
    #     return sol%(10**9+7)
