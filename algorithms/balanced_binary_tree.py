"""
Leetcode 110
Runtime: 64 ms, faster than 26.48% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 19.4 MB, less than 5.21% of Python3 online submissions for Balanced Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def _isBalanced(node):
            if not node:
                return True, 0
            left_balanced, left_height = _isBalanced(node.left)
            if not left_balanced:
                return False, -1
            right_balanced, right_height = _isBalanced(node.right)
            if not right_balanced:
                return False, -1
            return abs(right_height-left_height) <= 1, max(left_height, right_height)+1

        if not root:
            return True
        left_balanced, left_height = _isBalanced(root.left)
        if not left_balanced:
            return False
        right_balanced, right_height = _isBalanced(root.right)
        if not right_balanced:
            return False
        return abs(right_height-left_height) <= 1
