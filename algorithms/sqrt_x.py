"""
Leetcode 69
Runtime: 36 ms, faster than 54.92% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.1 MB, less than 75.45% of Python3 online submissions for Sqrt(x).
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        i, j = 1, x//2
        if x%2 != 0:
            j += 1
        while i < j:
            m = (i+j+1)//2
            if m*m > x:
                j = m-1
            else:
                i = m
        return i
