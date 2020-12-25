"""
Leetcode 498
December Leetcoding challenge
Runtime: 192 ms, faster than 67.79% of Python3 online submissions for Diagonal Traverse.
Memory Usage: 16.7 MB, less than 71.02% of Python3 online submissions for Diagonal Traverse.
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        i = j = 0
        sol = []
        m, n = len(matrix), len(matrix[0])
        up = True
        while i < m and j < n:
            sol += matrix[i][j],
            if up:
                i, j = i-1, j+1
            else:
                i, j = i+1, j-1
            if i < 0 or j >= n:
                i, j = i+1, j-1
                if j == n-1:
                    i += 1
                elif i == 0:
                    j += 1
                up = False
            elif j < 0 or i >= m:
                i, j = i-1, j+1
                if i == m-1:
                    j += 1
                elif j == 0:
                    i += 1
                up = True
        return sol
