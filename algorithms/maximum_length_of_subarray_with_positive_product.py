"""
Leetcode 1567
Runtime: 612 ms, faster than 85.66% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
Memory Usage: 28 MB, less than 60.00% of Python3 online submissions for Maximum Length of Subarray With Positive Product.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def helper(a, b):
            negs, first_neg, last_neg = 0, None, None
            for i in range(a, b):
                if nums[i] < 0:
                    negs += 1
                    if first_neg is None:
                        first_neg = i
                    last_neg = i
            return b-a if negs%2 == 0 else max(b-first_neg-1, last_neg-a)

        sol = i = 0
        for j in range(len(nums)+1):
            if j == len(nums) or nums[j] == 0:
                sol = max(sol, helper(i, j))
                i = j+1
        return sol
