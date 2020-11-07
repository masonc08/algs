"""
Leetcode 213
Runtime: 32 ms, faster than 58.12% of Python3 online submissions for House Robber II.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for House Robber II.
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(
            self._rob(nums, 0, len(nums)-1),
            self._rob(nums, 1, len(nums))
        )

    def _rob(self, nums, start, end):
        if len(nums) == 0:
            return 0
        if start-end == 1:
            return nums[start]
        pprev, prev = 0, nums[start]
        for i in range(start+1, end):
            pprev, prev = prev, max(prev, pprev+nums[i])
        return prev
