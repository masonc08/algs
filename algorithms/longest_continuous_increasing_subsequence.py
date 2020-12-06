"""
Leetcode 674
Runtime: 72 ms, faster than 75.33% of Python3 online submissions for Longest Continuous Increasing Subsequence.
Memory Usage: 15.4 MB, less than 19.26% of Python3 online submissions for Longest Continuous Increasing Subsequence.
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cur, sol = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += 1
                sol = max(cur, sol)
            else:
                cur = 1
        return sol
