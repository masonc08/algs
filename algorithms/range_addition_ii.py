"""
Leetcode 598
August Leetcoding challenge
O(n) runtime, O(1) space
Runtime: 68 ms, faster than 75.62% of Python3 online submissions for Range Addition II.
Memory Usage: 16.3 MB, less than 21.88% of Python3 online submissions for Range Addition II.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        max_x = min(ops, key=lambda x: x[0])
        max_y = min(ops, key=lambda x: x[1])
        return min(max_x[1], max_y[1])*min(max_x[0], max_y[0])
