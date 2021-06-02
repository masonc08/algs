"""
Leetcode 1124
O(n) runtime and space, psum-like solution
Runtime: 196 ms, faster than 95.90% of Python3 online submissions for Longest Well-Performing Interval.
Memory Usage: 14.8 MB, less than 72.31% of Python3 online submissions for Longest Well-Performing Interval.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        mp = {}
        csum = sol = 0
        for i, hr in enumerate(hours):
            csum += 1 if hr > 8 else -1
            if csum > 0:
                sol = i+1
            else:
                if csum-1 in mp:
                    sol = max(sol, i-mp[csum-1])
                if csum not in mp:
                    mp[csum] = i
        return sol

