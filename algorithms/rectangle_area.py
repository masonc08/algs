"""
Leetcode 223
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def get_overlap(a, b, c, d):
            return max(min(d, b)-max(c, a), 0)
        def get_area(a, b, c, d):
            return (c-a)*(d-b)
        return get_area(ax1, ay1, ax2, ay2) + get_area(bx1, by1, bx2, by2) - get_overlap(ax1, ax2, bx1, bx2)*get_overlap(ay1, ay2, by1, by2)
