"""
Leetcode 121
Runtime: 56 ms, faster than 92.83% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = (1<<31)-1
        highest = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif price-lowest > highest:
                highest = price-lowest
        return highest
