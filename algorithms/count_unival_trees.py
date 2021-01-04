"""
Daily Coding Problem #8, Leetcode 965
Runtime: 24 ms, faster than 96.09% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 14.4 MB, less than 14.84% of Python3 online submissions for Univalued Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def isUnivalTree(root):
            ct = 0
            lsol = rsol = True
            if root.left:
                lct, lsol = isUnivalTree(root.left)
                lsol = lsol and root.left.val == root.val
                ct += lct
            if root.right:
                rct, rsol = isUnivalTree(root.right)
                rsol = rsol and root.right.val == root.val
                ct += rct
            ct += lsol and rsol
            return ct, lsol and rsol
        ct, sol = isUnivalTree(root)
        print(ct)
        return sol
        