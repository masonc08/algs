"""
Leetcode 1339
August Leetcoding challenge
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
    MOD = 10**9+7
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_total = self._get_sum(root)
        sol, _ = self._get_max_prod(root, tree_total)
        return sol%self.MOD
    
    def _get_sum(self, root):
        return root.val + self._get_sum(root.left) + self._get_sum(root.right) if root else 0
    
    def _get_max_prod(self, root, tree_total):
        if not root:
            return 0, 0
        lmax, lttl = self._get_max_prod(root.left, tree_total)
        rmax, rttl = self._get_max_prod(root.right, tree_total)
        return (
            max((
                lmax,
                ((tree_total-lttl)*lttl),
                rmax,
                ((tree_total-rttl)*rttl)
            )), lttl + rttl + root.val
        )
        