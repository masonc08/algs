"""
Leetcode 136
Runtime: 124 ms, faster than 49.86% of Python3 online submissions for Single Number.
Memory Usage: 16.6 MB, less than 34.00% of Python3 online submissions for Single Number.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single