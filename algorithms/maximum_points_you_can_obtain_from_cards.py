"""
Leetcode 1423
Runtime: 432 ms, faster than 40.02% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
Memory Usage: 27.7 MB, less than 29.40% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
"""


class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        L = len(A)
        for i in range(1, L):
            A[i] += A[i-1]
        m = L-k
        if m == 0:
            return A[-1]
        window = A[m-1]
        for i in range(m, L):
            window = min(window, A[i]-A[i-m])
        return A[-1]-window