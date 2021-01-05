"""
Daily Coding Problem #9, Leetcode 198
Runtime: 28 ms, faster than 86.18% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 99.98% of Python3 online submissions for House Robber.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        pprev = 0
        for i in range(1, len(nums)):
            pprev, prev = prev, max(prev, pprev+nums[i])
        return prev
