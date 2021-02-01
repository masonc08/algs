"""
Leetcode 573
February Leetcoding challenge
O(n) runtime, O(1) space
Runtime: 152 ms, faster than 21.82% of Python3 online submissions for Squirrel Simulation.
Memory Usage: 15.1 MB, less than 41.82% of Python3 online submissions for Squirrel Simulation.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def _dist(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        nutsdist, d = 0, float('-inf')
        for nut in nuts:
            nutsdist += self._dist(nut, tree)*2
            d = max(d, self._dist(nut, tree)-self._dist(nut, squirrel))
        return nutsdist - d
