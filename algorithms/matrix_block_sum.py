"""
Leetcode 1314
O(mn) runtime and space by dp
Runtime: 104 ms, faster than 79.29% of Python3 online submissions for Matrix Block Sum.
Memory Usage: 15.3 MB, less than 61.09% of Python3 online submissions for Matrix Block Sum.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                above = mat[i-1][j] if i > 0 else 0
                left = mat[i][j-1] if j > 0 else 0
                diag = mat[i-1][j-1] if j > 0 and i > 0 else 0
                mat[i][j] = above + left - diag + mat[i][j]
        sol = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                i_up = max(0, i-k)
                i_down = min(m-1, i+k)
                j_left = max(0, j-k)
                j_right = min(n-1, j+k)
                sol[i][j] = sum((
                    mat[i_down][j_right],
                    -mat[i_down][j_left-1] if j_left > 0 else 0,
                    -mat[i_up-1][j_right] if i_up > 0 else 0,
                    mat[i_up-1][j_left-1] if j_left > 0 and i_up > 0 else 0
                ))
        return sol
