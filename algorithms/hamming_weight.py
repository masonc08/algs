"""
Leetcode 191
Part of Leetcode mock interview
Runtime: 24 ms, faster than 93.69% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 14 MB, less than 99.96% of Python3 online submissions for Number of 1 Bits.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        sol = 0
        while n:
            sol += 1
            n &= (n-1)
        return sol

"""
Cool 1 liner solution
Runtime: 28 ms, faster than 79.70% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 14.2 MB, less than 99.96% of Python3 online submissions for Number of 1 Bits.
"""
hammingWeight = lambda self, n: bin(n).count('1')