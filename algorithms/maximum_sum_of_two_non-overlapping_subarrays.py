"""
Leetcode 1031
Runtime: 48 ms, faster than 84.26% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
Memory Usage: 14.3 MB, less than 89.06% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
"""


class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        N = len(A)
        for i in range(1, N):
            A[i] += A[i-1]
        lmax, mmax, sol = A[L-1], A[M-1], A[L+M-1]
        for i in range(L+M, N):
            lmax = max(lmax, A[i-M]-A[i-M-L])
            mmax = max(mmax, A[i-L]-A[i-L-M])
            sol = max(sol, lmax+A[i]-A[i-M], mmax+A[i]-A[i-L])
        return sol
