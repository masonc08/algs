"""
Leetcode 331
August Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


"""
O(n) runtime, O(1) space
Runtime: 74 ms, faster than 5.63% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
Memory Usage: 14.3 MB, less than 44.60% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
"""
class Solution:
    def parse_string(self, preorder):
        for i, v in enumerate(preorder):
            if v == ',':
                yield preorder[i-1]
        yield preorder[-1]


    def isValidSerialization(self, preorder: str) -> bool:
        need = 1
        for v in self.parse_string(preorder):
            if need == 0:
                return False
            if v == '#':
                need -= 1
            else:
                need += 1
        return need == 0



"""
O(n) runtime and space
Runtime: 47 ms, faster than 11.27% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
Memory Usage: 14.4 MB, less than 15.81% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
"""
# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         if len(preorder) <= 2:
#             return preorder == '#'
#         if len(preorder) > 2 and preorder[-3:] != '#,#':
#             return False
#         return self._isValidSerialization(preorder) == len(preorder)


#     def _isValidSerialization(self, preorder: str, i=0) -> bool:
#         if preorder[i] == ',':
#             i += 1
#         if preorder[i] == '#':
#             return i+1
#         while preorder[i].isnumeric():
#             i += 1
#         i = self._isValidSerialization(preorder, i)
#         return self._isValidSerialization(preorder, i)
