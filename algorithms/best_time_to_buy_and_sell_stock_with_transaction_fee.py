"""
Leetcode 714
March Leetcoding challenge
Runtime: 700 ms, faster than 70.02% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 21.1 MB, less than 99.37% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        L = len(prices)
        if L <= 1:
            return 0
        have, not_have = -prices[0], 0
        for i in range(1, L):
            have, not_have = max(have, not_have-prices[i]), max(not_have, have+prices[i]-fee)
        return not_have
