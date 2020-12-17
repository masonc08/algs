"""
Leetcode 54
Runtime: 28 ms, faster than 80.93% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14.4 MB, less than 13.71% of Python3 online submissions for Spiral Matrix.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        sol, ctr = [0]*(m*n), 0
        i = j = end = 0
        while ctr < m*n:
            if end != 0:
                while ctr < m*n and i > end-1:
                    sol[ctr] = matrix[i][j]
                    i -= 1
                    ctr += 1
                i, j = i+1, j+1
            while ctr < m*n and j < n-end:
                sol[ctr] = matrix[i][j]
                j += 1
                ctr += 1
            i, j = i+1, j-1
            while ctr < m*n and i < m-end:
                sol[ctr] = matrix[i][j]
                i += 1
                ctr += 1
            i, j = i-1, j-1
            while ctr < m*n and j > end-1:
                sol[ctr] = matrix[i][j]
                j -= 1
                ctr += 1
            i, j = i-1, j+1
            end += 1
        return sol
