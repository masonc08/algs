"""
Leetcode 283
Runtime: 48 ms, faster than 77.77% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 17.87% of Python3 online submissions for Move Zeroes.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, v in enumerate(nums):
            if v:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
