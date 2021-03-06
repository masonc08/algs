"""
Leetcode 112
Runtime: 56 ms, faster than 84.45% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 41.00% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                sol += (prices[i]-prices[i-1])
        return sol
