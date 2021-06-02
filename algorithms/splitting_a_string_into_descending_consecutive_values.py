"""
Leetcode 1849
O(n^2) runtime O(n) space
Runtime: 28 ms, faster than 95.18% of Python3 online submissions for Splitting a String Into Descending Consecutive Values.
Memory Usage: 14.2 MB, less than 58.07% of Python3 online submissions for Splitting a String Into Descending Consecutive Values.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def splitString(self, s: str) -> bool:
        n = 0
        L = len(s)
        for i in range(L-1):
            c = int(s[i])
            n = n*10 + c
            if n != 0 and self.can_split_from(n, i+1, s, L):
                return True
        return False

    def can_split_from(self, pre: int, i: int, s: str, L: int) -> bool:
        if i == L:
            return True
        n = 0
        for j in range(i, L):
            c = int(s[j])
            n = n*10 + c
            if n > pre-1:
                return False
            if n != 0 and n == pre-1 and self.can_split_from(n, j+1, s, L):
                return True
        return n == pre-1
