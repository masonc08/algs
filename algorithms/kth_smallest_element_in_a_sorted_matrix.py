"""
Leetcode 378
Runtime: 256 ms, faster than 15.92% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 22.1 MB, less than 5.98% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""


import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], tar: int) -> int:
        m, n = len(matrix), len(matrix[0])
        h = [(matrix[0][0], 0, 0)]
        sol = 0
        for _ in range(tar):
            sol, i, j = heapq.heappop(h)
            i != m-1 and heapq.heappush(h, (matrix[i+1][j], i+1, j))
            j != n-1 and heapq.heappush(h, (matrix[i][j+1], i, j+1))
        return sol
