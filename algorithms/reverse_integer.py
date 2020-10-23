"""
Leetcode 7
Runtime: 28 ms, faster than 86.14% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 99.99% of Python3 online submissions for Reverse Integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        sol = 0
        while x != 0:
            sol *= 10
            sol += x%10
            if (neg and sol > 1<<31) or (not neg and sol > (1<<31)-1):
                return 0
            x //= 10
        return -sol if neg else sol
