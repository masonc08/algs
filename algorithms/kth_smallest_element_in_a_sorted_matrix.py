"""
Leetcode 378
"""


import heapq


class Solution:
    """
    Runtime: 164 ms, faster than 83.90% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    Memory Usage: 20.1 MB, less than 32.58% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    """
    def kthSmallest(self, matrix: List[List[int]], K: int) -> int:
        i, j = matrix[0][0], matrix[-1][-1]
        while i < j:
            m = (i+j)//2
            if self.rank(matrix, m) < K:
                i = m+1
            else:
                j = m
        return i
    
    def rank(self, matrix, m):
        i, j = len(matrix)-1, 0
        sol = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] > m:
                i -= 1
            else:
                sol += i+1
                j += 1
        return sol


    # Runtime: 256 ms, faster than 15.92% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 22.1 MB, less than 5.98% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # def kthSmallest(self, matrix: List[List[int]], tar: int) -> int:
    #     m, n = len(matrix), len(matrix[0])
    #     h = [(matrix[0][0], 0, 0)]
    #     sol = 0
    #     for _ in range(tar):
    #         sol, i, j = heapq.heappop(h)
    #         i != m-1 and heapq.heappush(h, (matrix[i+1][j], i+1, j))
    #         j != n-1 and heapq.heappush(h, (matrix[i][j+1], i, j+1))
    #     return sol
