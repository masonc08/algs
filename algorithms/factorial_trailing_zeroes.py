"""
Leetcode 172
Runtime: 32 ms, faster than 68.46% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 14.2 MB, less than 23.37% of Python3 online submissions for Factorial Trailing Zeroes.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        sol = 0
        while n:
            sol += (n//5)
            n //= 5
        return sol
