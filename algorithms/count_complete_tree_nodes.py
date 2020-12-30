"""
Leetcode 222
Runtime: 72 ms, faster than 83.85% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.6 MB, less than 10.45% of Python3 online submissions for Count Complete Tree Nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(node):
            i = 0
            while node:
                i += 1
                node = node.left
            return i

        l, r = height(root), height(root.right)+1 if root else 1
        sol = 2**l-1
        while l > 1:
            if l == r:
                root = root.right
            elif l > r:
                root = root.left
                sol -= 2**(r-1)
            l, r = height(root), height(root.right)+1 if root else 1
        return sol

