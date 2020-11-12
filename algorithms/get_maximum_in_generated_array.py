"""
Leetcode 1646
Leetcode weekly contest 214
Runtime: 28 ms, faster than 87.44% of Python3 online submissions for Get Maximum in Generated Array.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Get Maximum in Generated Array.
"""

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        c = 2
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        while c <= n:
            dp[c] = dp[c//2] if c%2==0 else dp[c//2]+dp[c//2+1]
            c += 1
        return max(dp)
