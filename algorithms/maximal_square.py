"""
Leetcode 221
Runtime: 224 ms, faster than 25.31% of Python3 online submissions for Maximal Square.
Memory Usage: 15.6 MB, less than 37.24% of Python3 online submissions for Maximal Square.
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sol = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] = int(matrix[i][j])
                if i != m-1 and j != n-1 and matrix[i][j] == 1:
                    s, e, se = matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]
                    matrix[i][j] = min(s, e, se)+1
                sol = max(sol, matrix[i][j])
        return sol*sol
