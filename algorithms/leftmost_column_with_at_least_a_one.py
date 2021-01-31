"""
Leetcode 1428
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
"""
O(M+N) runtime, O(1) space
Runtime: 104 ms, faster than 71.33% of Python3 online submissions for Leftmost Column with at Least a One.
Memory Usage: 14.4 MB, less than 96.43% of Python3 online submissions for Leftmost Column with at Least a One.
"""
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        i, j, sol = 0, n-1, -1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j):
                j, sol = j-1, j
            else:
                i += 1
        return sol

"""
O(nlogm) runtime, O(n) space
Runtime: 136 ms, faster than 12.55% of Python3 online submissions for Leftmost Column with at Least a One.
Memory Usage: 14.6 MB, less than 35.45% of Python3 online submissions for Leftmost Column with at Least a One.
"""
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         m, n = binaryMatrix.dimensions()
#         rem = set(range(m))
#         l, r = 0, n
#         while l < r:
#             m = l+r>>1
#             exist = set(i for i in rem if binaryMatrix.get(i, m))
#             if not exist:
#                 l = m+1
#             else:
#                 rem = exist
#                 r = m
#         return l if l != n else -1
