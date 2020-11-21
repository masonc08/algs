"""
Leetcode 81
Runtime: 56 ms, faster than 24.23% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 15.2 MB, less than 12.60% of Python3 online submissions for Search in Rotated Sorted Array II.
"""


import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[i] == nums[mid] == nums[j]:
                prev = (i, j)
                while nums[i] == nums[mid] and i < mid:
                    i += 1
                if nums[i] < nums[mid]:
                    break
                while i == mid and nums[mid] == nums[j] and j > mid:
                    j -= 1
                if nums[j] > nums[mid]:
                    i = j+1
                    break
                if i == j == mid:
                    if nums[j] != nums[-1]:
                        i = prev[0]
                    else:
                        if nums[0] < nums[j]:
                            i = 0
                        else:
                            i = prev[0]
                    break
            elif nums[i] <= nums[mid]:
                if nums[i] < nums[j]:
                    j = mid
                else:
                    i = mid+1
            else:
                j = mid
        start = i
        if i == len(nums)-1:
            if nums[0] < nums[-1]:
                start = 0
            else:
                start = len(nums)-1
        transform = lambda i, offset, size: (i+offset)%size
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if target == nums[transform(mid, start, len(nums))]:
                return True
            elif target > nums[transform(mid, start, len(nums))]:
                i = mid+1
            else:
                j = mid-1
        return nums[transform(i, start, len(nums))] == target
