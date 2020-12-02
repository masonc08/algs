"""
Leetcode 332
Runtime: 1224 ms, faster than 66.21% of Python3 online submissions for Coin Change.
Memory Usage: 14.2 MB, less than 91.96% of Python3 online submissions for Coin Change.
"""


import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != math.inf else -1

