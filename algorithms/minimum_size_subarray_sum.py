"""
Leetcode 209
Runtime: 64 ms, faster than 97.33% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 16.6 MB, less than 41.76% of Python3 online submissions for Minimum Size Subarray Sum.
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        j = cur = 0
        sol = float('inf')
        for i, v in enumerate(nums):
            cur += v
            while j <= i and cur >= s:
                sol = min(sol, i-j+1)
                cur -= nums[j]
                j += 1
        return sol if sol != float('inf') else 0
