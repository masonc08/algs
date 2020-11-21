"""
Leetcode 33
Runtime: 40 ms, faster than 62.25% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.4 MB, less than 79.91% of Python3 online submissions for Search in Rotated Sorted Array.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[i] <= nums[mid]:
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
                return transform(mid, start, len(nums))
            elif target > nums[transform(mid, start, len(nums))]:
                i = mid+1
            else:
                j = mid-1
        return transform(i, start, len(nums)) \
            if nums[transform(i, start, len(nums))] == target else -1
