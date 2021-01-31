"""
Leetcode 31
Runtime: 44 ms, faster than 44.52% of Python3 online submissions for Next Permutation.
Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Next Permutation.
"""


import bisect


"""
O(n) runtime, O(1) space by binary search
Runtime: 44 ms, faster than 54.18% of Python3 online submissions for Next Permutation.
Memory Usage: 14.2 MB, less than 56.18% of Python3 online submissions for Next Permutation.
"""
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        i = L-2
        while i > -1 and nums[i] >= nums[i+1]:
            i -= 1
        reverse(i+1, L-1)
        if i != -1:
            idx = bisect.bisect(nums, nums[i], i+1, L-1)
            nums[i], nums[idx] = nums[idx], nums[i]

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         last = float('-inf')
#         first = 0
#         for i in reversed(range(len(nums))):
#             cur = nums[i]
#             if cur < last:
#                 first = i+1
#                 for j in reversed(range(len(nums))):
#                     if nums[j] > cur:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break
#                 break
#             last = cur
#         i = first
#         j = len(nums)-1
#         while i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1