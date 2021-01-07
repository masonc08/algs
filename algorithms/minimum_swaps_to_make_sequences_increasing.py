"""
Leetcode 801
Runtime: 88 ms, faster than 56.31% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
Memory Usage: 14.6 MB, less than 37.89% of Python3 online submissions for Minimum Swaps To Make Sequences Increasing.
"""
# TODO: Consider revisiting


import functools


class Solution:
    def minSwap(self, A, B):
        N = len(A)
        not_swap, swap = 0, 1
        for i in range(1, N):
            not_swap2 = swap2 = N
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap2 = swap + 1
                not_swap2 = not_swap
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap2 = min(swap2, not_swap + 1)
                not_swap2 = min(not_swap2, swap)
            swap, not_swap = swap2, not_swap2
        return min(swap, not_swap)

# class Solution:
#     def minSwap(self, A, B):
#         @functools.lru_cache(None)
#         def swap(i):
#             if i == len(A):
#                 return 0
#             sol = float('inf')
#             if i == 0 or A[i] > A[i-1] and B[i] > B[i-1]:
#                 sol = min(sol, swap(i+1))
#             if i == 0 or B[i] > A[i-1] and A[i] > B[i-1]:
#                 A[i], B[i] = B[i], A[i]
#                 sol = min(sol, swap(i+1)+1)
#                 A[i], B[i] = B[i], A[i]
#             return sol
#         return swap(0)
