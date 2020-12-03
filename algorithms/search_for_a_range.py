"""
Leetcode 34
Runtime: 84 ms, faster than 55.94% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 20.69% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        i, j = 0, len(nums)-1
        while i <= j:
            m = (i+j)//2
            v = nums[m]
            if v == target:
                a = b = m
                while a != 0 and nums[a-1] == v:
                    a -= 1
                while b != len(nums)-1 and nums[b+1] == v:
                    b += 1
                return [a, b]
            elif v < target:
                i = m+1
            else:
                j = m-1
        return [-1, -1]
