"""
Leetcode 74
Runtime: 40 ms, faster than 79.29% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.7 MB, less than 9.43% of Python3 online submissions for Search a 2D Matrix.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n-1
        while i <= j:
            mid = (i+j)//2
            v = matrix[mid//m][mid%m]
            if v == target:
                return True
            elif v < target:
                i = mid+1
            else:
                j = mid-1
        return False
