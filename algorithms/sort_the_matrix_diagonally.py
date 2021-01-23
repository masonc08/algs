"""
Leetcode 1329
O(MNlogD) runtime, O(D) space, where D=min(M, N)
January Leetcoding challenge
Runtime: 96 ms, faster than 26.54% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.6 MB, less than 49.97% of Python3 online submissions for Sort the Matrix Diagonally
"""


import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def sort_diag(i0, j0):
            i, j, li = i0, j0, []
            while i < m and j < n:
                heapq.heappush(li, mat[i][j])
                i, j = i+1, j+1
            while li:
                mat[i0][j0] = heapq.heappop(li)
                i0, j0 = i0+1, j0+1

        for k in range(max(m, n)):
            k < m and sort_diag(k, 0)
            k < n and k != 0 and sort_diag(0, k)
        return mat