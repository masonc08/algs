"""
Leetcode 543
Runtime: 44 ms, faster than 67.32% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.4 MB, less than 9.60% of Python3 online submissions for Diameter of Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, node: TreeNode) -> int:
        def maxDepth(root):
            if not root:
                return 0, 0
            ldepth, lmax = maxDepth(root.left)
            rdepth, rmax = maxDepth(root.right)
            sol = max(lmax, rmax, ldepth+rdepth)
            return max(ldepth, rdepth)+1, sol
        
        _, sol = maxDepth(node)
        return sol
