"""
Leetcode 665
Runtime: 184 ms, faster than 74.25% of Python3 online submissions for Non-decreasing Array.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if c == 1:
                    return False
                if i == 0 or i == len(nums)-2:
                    c += 1
                else:
                    if nums[i-1] <= nums[i+1] or nums[i+2] >= nums[i]:
                        c += 1
                    else:
                        return False
        return True