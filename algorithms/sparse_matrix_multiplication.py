"""
Leetcode 311
O(max(A.rows, B.rows)*max(A.cols, B.cols)) runtime, O(A.rows*B.cols) space
Runtime: 52 ms, faster than 94.29% of Python3 online submissions for Sparse Matrix Multiplication.
Memory Usage: 14.8 MB, less than 40.06% of Python3 online submissions for Sparse Matrix Multiplication.
"""


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B[0])
        sol = [[0]*n for _ in range(m)]
        for i, row in enumerate(A):
            mp = { i1:v for i1, v in enumerate(row) if v }
            for j in range(n):
                sol[i][j] = sum(B[i1][j]*mp[i1] for i1 in mp )
        return sol
