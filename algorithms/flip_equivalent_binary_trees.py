"""
Leetcode 951
Runtime: 28 ms, faster than 89.06% of Python3 online submissions for Flip Equivalent Binary Trees.
Memory Usage: 14.3 MB, less than 24.79% of Python3 online submissions for Flip Equivalent Binary Trees.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if bool(root1) ^ bool(root2) or root1.val != root2.val:
            return False
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
            self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)     

