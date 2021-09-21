"""
Leetcode 918
Runtime: 632 ms, faster than 39.92% of Python3 online submissions for Maximum Sum Circular Subarray.
Memory Usage: 18.2 MB, less than 98.81% of Python3 online submissions for Maximum Sum Circular Subarray.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            cur = sol = next(nums, -math.inf)
            for v in nums:
                cur = max(cur+v, v)
                sol = max(cur, sol)
            return sol
        S = sum(nums)
        opt1 = S + kadane(-nums[i] for i in range(1, len(nums)))
        opt2 = S + kadane(-nums[i] for i in range(len(nums)-1))
        opt3 = kadane(iter(nums))
        return max(opt1, opt2, opt3)
