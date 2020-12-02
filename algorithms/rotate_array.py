"""
Leetcode 189
"""


from typing import List


class Solution:
    """
    In-place cycled reversing
    Runtime: 76 ms, faster than 20.11% of Python3 online submissions for Rotate Array.
    Memory Usage: 15.7 MB, less than 8.40% of Python3 online submissions for Rotate Array.
    """
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        k %= len(nums)
        if k == 0:
            return
        wrap = lambda i: (i+L)%L
        changed = offset = 0
        while changed < L:
            start = wrap(k+offset)
            i = offset
            changed += 1
            while i != start:
                nums[wrap(i+k)], nums[i] = nums[i], nums[wrap(i+k)]
                i = wrap(i-k)
                changed += 1
            offset += 1


    """
    In-place reversing
    Runtime: 60 ms, faster than 68.17% of Python3 online submissions for Rotate Array.
    Memory Usage: 15.7 MB, less than 8.40% of Python3 online submissions for Rotate Array.
    """
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     def reverse(i=0, j=len(nums)-1):
    #         while i < j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i, j = i+1, j-1

    #     k %= len(nums)
    #     if k == 0:
    #         return
    #     reverse()
    #     reverse(0, k-1)
    #     reverse(k, len(nums)-1)


Solution().rotate([1,2,3,4,5,6], 3)