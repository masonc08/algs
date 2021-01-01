"""
Leetcode 442
Runtime: 400 ms, faster than 18.17% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.4 MB, less than 89.88% of Python3 online submissions for Find All Duplicates in an Array.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i]-1 != i and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [v for i, v in enumerate(nums) if v != i+1]
