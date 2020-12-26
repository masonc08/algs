"""
Leetcode 279
Runtime: 4484 ms, faster than 33.79% of Python3 online submissions for Perfect Squares.
Memory Usage: 14.2 MB, less than 78.57% of Python3 online submissions for Perfect Squares.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        A = []
        i = 1
        while i*i <= n:
            A += i*i,
            i += 1
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for nat in A:
                if nat <= i:
                    dp[i] = min(1+dp[i-nat], dp[i])
        return dp[-1]
