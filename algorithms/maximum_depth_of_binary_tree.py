"""
Leetcode 104
December Leetcoding challenge
Runtime: 36 ms, faster than 89.53% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.1 MB, less than 17.75% of Python3 online submissions for Maximum Depth of Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
