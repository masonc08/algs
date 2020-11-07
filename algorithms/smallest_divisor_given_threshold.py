"""
Leetcode 1283
November Leetcoding challenge
Runtime: 440 ms, faster than 56.17% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
Memory Usage: 19.9 MB, less than 80.03% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
"""

import math
from typing import List

# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:
#         lo = 1
#         hi = max(nums)
#         mid = (lo+hi)//2
#         cur = 0
#         while lo < hi:
#             mid = (lo+hi)//2
#             cur = self._sum(nums, mid)
#             if cur > threshold:
#                 lo = mid+1
#             elif cur < threshold:
#                 hi = mid
#             else:
#                 break
#         while mid > 1 and self._sum(nums, mid-1) == cur:
#             mid -= 1
#         return mid
        
#     def _sum(self, li, divi):
#         sol = 0
#         for num in li:
#             sol += math.ceil(num//divi)
#         return sol

# Solution().smallestDivisor([1, 2, 5, 9], 6)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            num = self._sum(nums, mid)
            if num > threshold:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def _sum(self, li, divi):
        sol = 0
        for num in li:
            sol += math.ceil(num/divi)
        return sol
