"""
Leetcode 53
Runtime: 68 ms, faster than 51.43% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.8 MB, less than 88.00% of Python3 online submissions for Maximum Subarray.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        last = sol = nums[0]
        cur = 0
        for i in range(1, len(nums)):
            cur = max(last+nums[i], nums[i])
            sol = max(sol, cur)
            last = cur
        return sol
