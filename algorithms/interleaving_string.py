"""
Leetcode 97
June Leetcoding challenge
O(nm) runtime, O(n*m) space
Runtime: 44 ms, faster than 35.85% of Python3 online submissions for Interleaving String.
Memory Usage: 14.7 MB, less than 10.66% of Python3 online submissions for Interleaving String.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return len(s1) + len(s2) == len(s3) and \
                (self._isInterleave(0, 0, s1, s2, s3) or \
                self._isInterleave(0, 0, s2, s1, s3))

    @functools.lru_cache(None)
    def _isInterleave(self, a, b, s1: str, s2: str, s3: str) -> bool:
        L1, L2 = len(s1), len(s2)
        if a == L1 and b == L2:
            return True
        while a < L1 and s1[a] == s3[a+b]:
            if self._isInterleave(b, a+1, s2, s1, s3):
                return True
            a += 1
        return False

