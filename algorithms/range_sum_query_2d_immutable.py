"""
Leetcode 304
"""


from typing import List


class NumMatrix:
    """
    Cache cumulative sums by area relative to origin, O(m*n) space, O(1) runtime
    Runtime: 104 ms, faster than 82.68% of Python3 online submissions for Range Sum Query 2D - Immutable.
    Memory Usage: 17.2 MB, less than 11.66% of Python3 online submissions for Range Sum Query 2D - Immutable.
    """
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cache = [[None]*len(self.matrix[0]) for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                a = self.cache[i][j-1] if j != 0 else 0
                b = self.cache[i-1][j] if i != 0 else 0
                c = self.cache[i-1][j-1] if i != 0 and j != 0 else 0
                self.cache[i][j] = a+b-c+self.matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.cache[row1-1][col2] if row1 != 0 else 0
        b = self.cache[row2][col1-1] if col1 != 0 else 0
        c = self.cache[row1-1][col1-1] if row1 != 0 and col1 != 0 else 0
        d = self.cache[row2][col2]
        return d-b-a+c


    """
    Spin up bidirectional cumulative sum cache on the fly, O(m*n) space, O(n*min(l, w)) runtime
    Runtime: 296 ms, faster than 22.36% of Python3 online submissions for Range Sum Query 2D - Immutable.
    Memory Usage: 17.4 MB, less than 7.15% of Python3 online submissions for Range Sum Query 2D - Immutable.
    """
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
    #     self.row_cache = [[None]*(len(matrix[0])+1) for _ in range(len(matrix))]
    #     self.col_cache = [[None]*len(matrix[0]) for _ in range(len(matrix)+1)]


    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sol = 0
    #     if row2-row1 > col2-col1:
    #         for i in range(col1, col2+1):
    #             if self.col_cache[row2][i] is None:
    #                 ptr = 0 if self.col_cache[-1][i] is None else self.col_cache[-1][i]
    #                 for j in range(ptr, row2+1):
    #                     x = self.col_cache[j-1][i] if j != 0 else 0
    #                     self.col_cache[j][i] = self.matrix[j][i]+x
    #                     ptr += 1
    #                 self.col_cache[-1][i] = ptr
    #             x = self.col_cache[row1-1][i] if row1 != 0 else 0
    #             sol += (self.col_cache[row2][i]-x)
    #     else:
    #         for i in range(row1, row2+1):
    #             if self.row_cache[i][col2] is None:
    #                 ptr = 0 if self.row_cache[i][-1] is None else self.row_cache[i][-1]
    #                 for j in range(ptr, col2+1):
    #                     x = self.row_cache[i][j-1] if j != 0 else 0
    #                     self.row_cache[i][j] = self.matrix[i][j]+x
    #                     ptr += 1
    #                 self.row_cache[i][-1] = ptr
    #             x = self.row_cache[i][col1-1] if col1 != 0 else 0
    #             sol += (self.row_cache[i][col2]-x)
    #     return sol

    """
    Create bidirectional cumulative sum cache, O(m*n) space, O(n*min(l, w)) runtime
    Runtime: 220 ms, faster than 33.14% of Python3 online submissions for Range Sum Query 2D - Immutable.
    Memory Usage: 17.4 MB, less than 7.15% of Python3 online submissions for Range Sum Query 2D - Immutable.
    """
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix 
    #     self.row_cache = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    #     self.col_cache = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             self.row_cache[i][j] = self.matrix[i][j] if j == 0 else self.matrix[i][j]+self.row_cache[i][j-1]
    #             self.col_cache[i][j] = self.matrix[i][j] if i == 0 else self.matrix[i][j]+self.col_cache[i-1][j]
        

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sol = 0
    #     if row2-row1 > col2-col1:
    #         for i in range(col1, col2+1):
    #             x = self.col_cache[row1-1][i] if row1 != 0 else 0
    #             sol += (self.col_cache[row2][i]-x)
    #     else:
    #         for i in range(row1, row2+1):
    #             x = self.row_cache[i][col1-1] if col1 != 0 else 0
    #             sol += (self.row_cache[i][col2]-x)
    #     return sol


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
