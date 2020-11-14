"""
Leetcode 236
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Recursive solution by surfacing nodes
    Runtime: 64 ms, faster than 93.74% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    Memory Usage: 24.9 MB, less than 46.60% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol, _ = self._lowestCommonAncestor(root, p, q)
        return sol

    def _lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root, False
        left, found_left = self._lowestCommonAncestor(root.left, p, q)
        right, found_right = self._lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root, True
        if left:
            if found_left:
                return left, True
            return left, False
        if right:
            if found_right:
                return right, True
            return right, False
        return None, False

    """
    Recursive solution by recording paths
    Runtime: 84 ms, faster than 22.18% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    Memory Usage: 27 MB, less than 34.83% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    """
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     def traverse(run, node, path):
    #         if not run:
    #             return False
    #         path.append(run)
    #         if run is node:
    #             return True
    #         if traverse(run.left, node, path):
    #             return True
    #         if traverse(run.right, node, path):
    #             return True
    #         path.pop()
    #         return False

    #     a, b = [], []
    #     traverse(root, p, a)
    #     traverse(root, q, b)
    #     shorter = min(a, b, key=len)
    #     i = len(shorter)-1
    #     while a[i] is not b[i]:
    #         i -= 1
    #     return a[i]
