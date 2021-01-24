"""
Daily Coding Problem #3, Leetcode 41
Runtime: 32 ms, faster than 84.33% of Python3 online submissions for First Missing Positive.
Memory Usage: 14.2 MB, less than 63.14% of Python3 online submissions for First Missing Positive.
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = len(nums)
        for i in range(L):
            while 1 <= nums[i] <= L and nums[i] != nums[nums[i]-1]:
                other = nums[i]-1
                nums[i], nums[other] = nums[other], nums[i]
        for i, v in enumerate(nums):
            if v-1 != i:
                return i+1
        return L+1

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         base = float('inf')
#         L = len(nums)
#         positives = L
#         for n in nums:
#             if n > 0:
#                 base = min(base, n)
#             else:
#                 positives -= 1
#         if base > 1:
#             return 1
#         # lowest positive has to be 1
#         for i in range(L):
#             while 1 <= nums[i] <= positives and nums[i] != i+1:
#                 other = nums[i]-1
#                 if nums[other] == nums[i]:
#                     break
#                 nums[i], nums[other] = nums[other], nums[i]
#         for i, v in enumerate(nums):
#             if v != i+1:
#                 return i+1
#         return nums[-1]+1
