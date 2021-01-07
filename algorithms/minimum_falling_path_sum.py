"""
Leetcode 931
Runtime: 104 ms, faster than 98.18% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 15.4 MB, less than 16.87% of Python3 online submissions for Minimum Falling Path Sum.
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        for i in range(N-2, -1, -1):
            for j in range(N):
                A[i][j] += min(
                    A[i+1][j-1] if j != 0 else float('inf'),
                    A[i+1][j],
                    A[i+1][j+1] if j != N-1 else float('inf')
                )
        return min(A[0])
