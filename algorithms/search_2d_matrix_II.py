"""
Leetcode 240
"""


from typing import List


class Solution:
    """
    Snaking through matrix
    Runtime: 164 ms, faster than 9.70% of Python3 online submissions for Search a 2D Matrix II.
    Memory Usage: 20.4 MB, less than 13.58% of Python3 online submissions for Search a 2D Matrix II.
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            v = matrix[i][j]
            if v < target:
                i += 1
            elif v > target:
                j -= 1
            else:
                return True
        return False


    """
    Binary searching with divide and conquer
    Runtime: 164 ms, faster than 9.70% of Python3 online submissions for Search a 2D Matrix II.
    Memory Usage: 20.6 MB, less than 10.10% of Python3 online submissions for Search a 2D Matrix II.
    """
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     s, e = 0, len(matrix[0])-1
    #     while s < e:
    #         m = (s+e+1)//2
    #         v = matrix[0][m]
    #         if v < target:
    #             s = m
    #         elif v > target:
    #             e = m-1
    #         else:
    #             return True
    #     if matrix[0][s] == target:
    #         return True
    #     a = s
    #     s, e = 0, len(matrix[-1])-1
    #     while s < e:
    #         m = (s+e)//2
    #         v = matrix[-1][m]
    #         if v < target:
    #             s = m+1
    #         elif v > target:
    #             e = m
    #         else:
    #             return True
    #     if matrix[-1][s] == target:
    #         return True
    #     b = s
    #     llim, rlim = 1, len(matrix)-2
    #     for i in range(b, ((a+b)//2)+1):
    #         if llim >= len(matrix) or rlim >= len(matrix):
    #             return False
    #         s, e = llim, rlim
    #         while s <= e:
    #             m = (s+e)//2
    #             v = matrix[m][i]
    #             if v == target:
    #                 return True
    #             elif v < target:
    #                 s = m+1
    #             else:
    #                 rlim = m-1
    #                 e = m-1
    #         s, e = llim, rlim
    #         while s <= e:
    #             m = (s+e)//2
    #             v = matrix[m][a+b-i]
    #             if v == target:
    #                 return True
    #             elif v < target:
    #                 llim = m+1
    #                 s = m+1
    #             else:
    #                 e = m-1
    #     return False
