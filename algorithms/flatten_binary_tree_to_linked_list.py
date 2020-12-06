"""
Leetcode 114
Runtime: 40 ms, faster than 42.88% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.2 MB, less than 9.58% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        left_leaf = self.flatten(root.left) if root.left else None
        right_leaf = self.flatten(root.right) if root.right else None
        if root.left and root.right:
            root.right, left_leaf.right = root.left, root.right
        elif root.left:
            root.right = root.left
        root.left = None
        return right_leaf or left_leaf
