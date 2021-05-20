"""
Leetcode 462
May Leetcoding challenge
Runtime: 76 ms, faster than 49.69% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
Memory Usage: 15.3 MB, less than 75.16% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


import statistics

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        center = round(statistics.median(nums))
        return sum(abs(center-v) for v in nums)

