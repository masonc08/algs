"""
Leetcode 235
Runtime: 72 ms, faster than 88.21% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.1 MB, less than 42.30% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lo, hi = sorted([p.val, q.val])
        run = root
        while run and (not (lo <= run.val <= hi)):
            if run.val > hi:
                run = run.left
            elif run.val < lo:
                run = run.right
        if not run:
            raise Exception("The provided nodes do not exist in the tree")
        return run.val
