"""
Leetcode 704
Classic binary search
Runtime: 240 ms, faster than 27.89% of Python3 online submissions for Binary Search.
Memory Usage: 15.3 MB, less than 40.94% of Python3 online submissions for Binary Search.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            m = (i+j)//2
            v = nums[m]
            if v == target:
                return m
            elif v < target:
                i = m+1
            else:
                j = m-1
        return i if nums[i] == target else -1
