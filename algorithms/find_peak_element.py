"""
Leetcode 162
"""


import math


class Solution:
    """
    O(logn) runtime, O(1) space by binary searching
    Runtime: 48 ms, faster than 28.27% of Python3 online submissions for Find Peak Element.
    Memory Usage: 14.5 MB, less than 12.54% of Python3 online submissions for Find Peak Element.
    """
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-2
        while l < r:
            m = (l+r)//2
            if nums[m+1] > nums[m]:
                l = m+1
            else:
                r = m
        if l == len(nums)-2:
            if nums[l] < nums[l+1]:
                return len(nums)-1
        return l


    """
    O(n) runtime, O(1) space by linear scanning
    Runtime: 44 ms, faster than 65.71% of Python3 online submissions for Find Peak Element.
    Memory Usage: 14.5 MB, less than 12.54% of Python3 online submissions for Find Peak Element.
    """
    # def findPeakElement(self, nums: List[int]) -> int:
    #     for i, v in enumerate(nums):
    #         l = nums[i-1] if i != 0 else -math.inf
    #         r = nums[i+1] if i != len(nums)-1 else -math.inf
    #         if l < v > r:
    #             return i
    #     raise Exception()
