"""
Leetcode 69
"""


class Solution:
    """
    Integer newton's method for sqrtx
    Runtime: 28 ms, faster than 92.03% of Python3 online submissions for Sqrt(x).
    Memory Usage: 14.1 MB, less than 78.67% of Python3 online submissions for Sqrt(x).
    """
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        prev = x
        while 1:
            cur = (prev+x//prev)//2
            if cur >= prev:
                return prev
            prev = cur

    """
    Binary search
    Runtime: 36 ms, faster than 54.92% of Python3 online submissions for Sqrt(x).
    Memory Usage: 14.1 MB, less than 75.45% of Python3 online submissions for Sqrt(x).
    """
    # def mySqrt(self, x: int) -> int:
    #     if x <= 1:
    #         return x
    #     i, j = 1, x//2
    #     if x%2 != 0:
    #         j += 1
    #     while i < j:
    #         m = (i+j+1)//2
    #         if m*m > x:
    #             j = m-1
    #         else:
    #             i = m
    #     return i
