"""
Leetcode 698
September Leetcoding challenge
Runtime: 140 ms, faster than 37.06% of Python3 online submissions for Partition to K Equal Sum Subsets.
Memory Usage: 14.2 MB, less than 78.07% of Python3 online submissions for Partition to K Equal Sum Subsets.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        tar, rem = divmod(sum(nums), k)
        if rem != 0:
            return False
        def helper(cur, k, i=0):
            if cur == tar:
                return helper(0, k-1, 0) if k != 1 else True
            if cur > tar or i == len(nums):
                return False
            if nums[i] < 0:
                return helper(cur, k, i+1)
            nums[i] = -nums[i]
            if helper(cur-nums[i], k, i+1):
                return True
            nums[i] = -nums[i]
            if helper(cur, k, i+1):
                return True
        return helper(0, k)
