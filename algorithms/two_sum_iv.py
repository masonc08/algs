"""
Leetcode 653
August Leetcoding challenge
O(n) runtime, O(d) space
Runtime: 96 ms, faster than 31.95% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 16.3 MB, less than 87.72% of Python3 online submissions for Two Sum IV - Input is a BST.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, node, normal=True):
        self.stk = [node] if node else []
        self.normal = normal
        self._sync()
    
    def has_next(self):
        return len(self.stk) != 0

    def get_next(self):
        if not self.has_next():
            raise Exception("There are no more elements")
        sol = self.stk.pop()
        if (sol.right if self.normal else sol.left):
            self.stk.append(sol.right if self.normal else sol.left)
            self._sync()
        return sol.val

    def _sync(self):
        if not self.has_next():
            return
        node = self.stk[-1]
        while (node.left if self.normal else node.right):
            node = node.left if self.normal else node.right
            self.stk.append(node)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        fwd, bkwd = BSTIterator(root, True), BSTIterator(root, False)
        a, b = fwd.get_next(), bkwd.get_next()
        while a != b:
            if a+b > k:
                b = bkwd.get_next()
            elif a+b < k:
                a = fwd.get_next()
            else:
                return True
        return False
