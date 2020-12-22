"""
Leetcode 908
Runtime: 108 ms, faster than 82.13% of Python3 online submissions for Smallest Range I.
Memory Usage: 15.3 MB, less than 43.24% of Python3 online submissions for Smallest Range I.
"""


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A)-min(A)-2*K)
