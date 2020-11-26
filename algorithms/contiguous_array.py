"""
Leetcode 525
Runtime: 948 ms, faster than 8.40% of Python3 online submissions for Contiguous Array.
Memory Usage: 18.7 MB, less than 92.55% of Python3 online submissions for Contiguous Array.
"""


import collections


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = collections.defaultdict(lambda: len(nums))
        mp[0] = -1
        ct = 0
        sol = 0
        for i, v in enumerate(nums):
            if v == 0:
                ct -= 1
            if v == 1:
                ct += 1
            if ct in mp:
                sol = max(sol, i-mp[ct])
            mp[ct] = min(mp[ct], i)
        return sol


    # def findMaxLength(self, nums: List[int]) -> int:
    #     i, j = 0, len(nums)-1
    #     offset = 2*sum(nums)-len(nums)
    #     while i < j:
    #         if offset > 0:
    #             if nums[i] == 0 and nums[j] == 0:
    #                 a, b = i, j
    #                 while a < b:
    #                     if a == 1:
    #                         i = a
    #                         offset += (i-a)
    #                         break
    #                     if b == 1:
    #                         j = b
    #                         offset += (b-j)
    #                         break
    #                     a += 1
    #                     b -= 1
    #                 if a == b:
    #                     return 0
    #             elif nums[i] == 1:
    #                 offset -= 1
    #                 i += 1
    #             elif nums[j] == 1:
    #                 offset -= 1
    #                 j -= 1
    #         elif offset < 0:
    #             if nums[i] == 1 and nums[j] == 1:
    #                 a, b = i, j
    #                 while a < b:
    #                     if a == 0:
    #                         offset -= (i-a)
    #                         i = a
    #                         break
    #                     if b == 0:
    #                         offset -= (b-j)
    #                         j = b
    #                         break
    #                     a += 1
    #                     b -= 1
    #                 if a == b:
    #                     return 0
    #             elif nums[i] == 0:
    #                 offset += 1
    #                 i += 1
    #             elif nums[j] == 0:
    #                 offset += 1
    #                 j -= 1
    #         elif offset == 0:
    #             return j-i+1
    #     return 0
