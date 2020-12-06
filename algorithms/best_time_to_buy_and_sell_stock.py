"""
Leetcode 121
"""
 

class Solution:
    """
    Dynamic program using Kadane's Algorithm
    Runtime: 68 ms, faster than 38.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 14.9 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """
    # def maxProfit(self, prices: List[int]) -> int:
    #     prev = sol = 0
    #     for i in range(1, len(prices)):
    #         incr = prices[i]-prices[i-1]
    #         prev = max(prev+incr, 0)
    #         sol = max(sol, prev)
    #     return sol


"""
Runtime: 56 ms, faster than 92.83% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         lowest = (1<<31)-1
#         highest = 0
#         for price in prices:
#             if price < lowest:
#                 lowest = price
#             elif price-lowest > highest:
#                 highest = price-lowest
#         return highest
