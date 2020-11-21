"""
Leetcode 338
"""


import math


class Solution:
    """
    Runtime: 68 ms, faster than 98.90% of Python3 online submissions for Counting Bits.
    Memory Usage: 21 MB, less than 7.89% of Python3 online submissions for Counting Bits.
    """
    def countBits(self, num: int) -> List[int]:
        sol = [0]*(num+1)
        for i in range(1, num+1):
            sol[i] = sol[i>>1]+(i&1)
        return sol

    """
    Using logarithm
    Runtime: 96 ms, faster than 35.34% of Python3 online submissions for Counting Bits.
    Memory Usage: 21 MB, less than 7.89% of Python3 online submissions for Counting Bits.
    """
    # def countBits(self, num: int) -> List[int]:
    #     sol = [0]*(num+1)
    #     for i in range(1, num+1):
    #         prev = i-1
    #         new = i
    #         x = prev^new
    #         x >>= 1
    #         x += 1
    #         sol[i] = sol[i-1]+1-int(math.log2(x))
    #     return sol
