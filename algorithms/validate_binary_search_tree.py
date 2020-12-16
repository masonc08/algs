"""
Leetcode 98
Runtime: 48 ms, faster than 33.46% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.4 MB, less than 52.57% of Python3 online submissions for Validate Binary Search Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, l=float('-inf'), h=float('inf')) -> bool:
        if not root:
            return True
        if root.val < l or root.val > h:
            return False
        return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val+1, h) 
