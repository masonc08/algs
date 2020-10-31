"""
Leetcode 371
Runtime: 20 ms, faster than 98.28% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 14 MB, less than 99.87% of Python3 online submissions for Sum of Two Integers.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ceil = (1<<31)-1
        mask = (1<<32)-1
        while b != 0:
            tmp = (a^b)&mask
            b = ((a&b)<<1)&mask
            a = tmp
        return a if a <= ceil else ~(a^mask)
        