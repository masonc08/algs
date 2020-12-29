"""
Leetcode 309
Runtime: 36 ms, faster than 83.80% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 14.5 MB, less than 68.71% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        if L == 0:
            return 0
        has0donothing = has1sell = 0
        has0buy = has1donothing = -prices[0]
        for i in range(1, L):
            has0donothing, has1sell, has0buy, has1donothing = (
                max(has0donothing, has1sell),
                max(has1donothing, has0buy) + prices[i],
                has0donothing - prices[i],
                max(has0buy, has1donothing)
            )
        return max(has1sell, has0donothing)
