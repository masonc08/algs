"""
Leetcode 1732
Leetcode biweekly contest 44
O(N) runtime, O(1) space
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find the Highest Altitude.
"""


from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
