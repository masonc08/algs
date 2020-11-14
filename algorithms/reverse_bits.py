"""
Leetcode 190
Runtime: 32 ms, faster than 59.95% of Python3 online submissions for Reverse Bits.
Memory Usage: 14.2 MB, less than 24.55% of Python3 online submissions for Reverse Bits.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        c = 0
        sol = 0
        while n or c < 32:
            bit = n&1
            n >>= 1
            sol <<= 1
            sol |= bit
            c += 1
        return sol
