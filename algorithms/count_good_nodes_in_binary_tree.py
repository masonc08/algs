"""
Leetcode 1448
Runtime: 284 ms, faster than 21.23% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 33.4 MB, less than 6.52% of Python3 online submissions for Count Good Nodes in Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, highest=-0x7fffffff-1) -> int:
        if not root:
            return 0
        sol = self.goodNodes(root.left, max(root.val, highest)) + \
            self.goodNodes(root.right, max(root.val, highest))
        if root.val >= highest:
            sol += 1
        return sol
