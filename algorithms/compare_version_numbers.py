"""
Leetcode 165
Runtime: 28 ms, faster than 87.10% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 14 MB, less than 99.40% of Python3 online submissions for Compare Version Numbers.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j, L1, L2 = 0, 0, len(version1), len(version2)
        while i < L1 or j < L2:
            v1 = v2 = 0
            while i < L1 and version1[i] != '.':
                v1 = v1*10 + int(version1[i])
                i += 1
            i += 1
            while j < L2 and version2[j] != '.':
                v2 = v2*10 + int(version2[j])
                j += 1
            j += 1
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
