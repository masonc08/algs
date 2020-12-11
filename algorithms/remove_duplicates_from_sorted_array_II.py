"""
Leetcode 80
December Leetcoding challenge
Runtime: 60 ms, faster than 13.99% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14.2 MB, less than 34.56% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = cur = 0
        while j < len(nums):
            nums[i] = nums[j]
            i += 1
            cur += 1
            j += 1
            while j < len(nums) and nums[i-1] == nums[j]:
                if cur < 2:
                    nums[i] = nums[j]
                    cur += 1
                    i += 1
                j += 1
            cur = 0
        return i
