"""
Leetcode 0
July Leetcoding challenge
Runtime: 24 ms, faster than 95.99% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 13.9 MB, less than 98.95% of Python3 online submissions for Binary Tree Pruning.
O(n) runtime, O(h) space from recursion
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return None if not root.left and not root.right and root.val == 0 else root   
        