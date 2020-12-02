"""
Leetcode 189
Runtime: 60 ms, faster than 68.17% of Python3 online submissions for Rotate Array.
Memory Usage: 15.7 MB, less than 8.40% of Python3 online submissions for Rotate Array.
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i=0, j=len(nums)-1):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1

        k %= len(nums)
        if k == 0:
            return
        reverse()
        reverse(0, k-1)
        reverse(k, len(nums)-1)
