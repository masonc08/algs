"""
Leetcode 1007
Runtime: 1364 ms, faster than 10.11% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 15.3 MB, less than 32.01% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
"""


import collections


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        L = len(A)
        cur = set()
        cta, ctb = collections.Counter(), collections.Counter()
        for i in range(L):
            if i == 0:
                cur |= set([ A[i], B[i] ])
            else:
                cur &= set([ A[i], B[i] ])
            if not cur:
                return -1
            cta[A[i]] += 1
            ctb[B[i]] += 1
        sol = L
        for i in cur:
            sol = min(sol, L-max(cta[i], ctb[i]))
        return sol
