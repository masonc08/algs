"""
Leetcode 35
Runtime: 48 ms, faster than 63.32% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.5 MB, less than 78.08% of Python3 online submissions for Search Insert Position.
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            m = (i+j)//2
            v = nums[m]
            if v == target:
                return m
            elif target > v:
                i = m+1
            else:
                j = m
        return i
