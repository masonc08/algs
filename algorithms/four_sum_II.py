"""
Leetcode 454
"""


from typing import List
from collections import defaultdict


class Solution:
    """
    O(n^2) runtime and space solution
    Runtime: 268 ms, faster than 73.56% of Python3 online submissions for 4Sum II.
    Memory Usage: 56 MB, less than 24.98% of Python3 online submissions for 4Sum II.
    """
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mp = defaultdict(int)
        for a in A:
            for b in B:
                mp[a+b] += 1
        sol = 0
        for c in C:
            for d in D:
                sol += mp[-c-d]
        return sol


    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    #     A.sort(), B.sort(), C.sort(), D.sort()
    #     sol = 0
    #     multiplier_a = 1
    #     for a, num_a in enumerate(A):
    #         if a+1 < len(A) and A[a+1] == num_a:
    #             multiplier_a += 1
    #             continue
    #         cur = num_a
    #         multiplier_b = 1
    #         for b, num_b in enumerate(B):
    #             if b+1 < len(B) and B[b+1] == num_b:
    #                 multiplier_b += 1
    #                 continue
    #             cur += num_b
    #             i, j = 0, len(D)-1
    #             while i < len(C) and j >= 0:
    #                 ttl = C[i] + D[j]
    #                 if ttl+cur == 0:
    #                     x = y = 1
    #                     while i < len(C)-1 and C[i] == C[i+1]:
    #                         x += 1
    #                         i += 1
    #                     while j >= 1 and D[j] == D[j-1]:
    #                         y += 1
    #                         j -= 1
    #                     sol += x*y*multiplier_a*multiplier_b
    #                     i += 1
    #                     j -= 1
    #                 elif ttl+cur > 0:
    #                     j -= 1
    #                 else:
    #                     i += 1
    #             cur -= num_b
    #             multiplier_b = 1
    #         multiplier_a = 1
    #     return sol

