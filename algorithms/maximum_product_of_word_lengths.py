"""
Leetcode 318
May Leetcoding challenge
Runtime: 2444 ms, faster than 28.57% of Python3 online submissions for Maximum Product of Word Lengths.
Memory Usage: 15 MB, less than 26.27% of Python3 online submissions for Maximum Product of Word Lengths.
O(nm^2) runtime, O(m) space, where n=len(strs), m=len(words)
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        L = len(words)
        occs = [[False]*26 for _ in range(L)]
        for word, occ in zip(words, occs):
            for c in word:
                i = ord(c) - ord('a')
                occ[i] = True
        sol = 0
        for i in range(L-1):
            for j in range(i+1, L):
                if self.no_overlap(occs[i], occs[j]):
                    sol = max(sol, len(words[i])*len(words[j]))
        return sol

    def no_overlap(self, occA, occB):
        return not any(a and b for a, b in zip(occA, occB))

