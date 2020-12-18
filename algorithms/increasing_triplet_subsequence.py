"""
Leetcode 334
Runtime: 52 ms, faster than 76.05% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 14.9 MB, less than 7.12% of Python3 online submissions for Increasing Triplet Subsequence.
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = 0x7fffffff, 0x7fffffff
        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True
        return False
