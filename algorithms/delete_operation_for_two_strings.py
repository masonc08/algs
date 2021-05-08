"""
Leetcode 583
May Leetcoding challenge
Runtime: 220 ms, faster than 98.46% of Python3 online submissions for Delete Operation for Two Strings.
Memory Usage: 14.4 MB, less than 94.69% of Python3 online submissions for Delete Operation for Two Strings.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m = len(A)
        sol = [0]*m
        for b in B:
            new = [0]*m
            for j, a in enumerate(A):
                if a == b:
                    new[j] += 1
                    if j != 0:
                        new[j] += sol[j-1]
                else:
                    tmp = sol[j]
                    if j != 0:
                        tmp = max(tmp, new[j-1])
                    new[j] += tmp
            sol = new
        return sol[-1]

    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1) + len(word2) - self.longestCommonSubsequence(word1, word2)*2

