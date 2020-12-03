"""
Leetcode 897
December Leetcoding challenge
Runtime: 32 ms, faster than 59.42% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 14.3 MB, less than 6.40% of Python3 online submissions for Increasing Order Search Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def make_tree(node, sol):
            if not node:
                return sol
            tail = make_tree(node.left, sol)
            tail.right = node
            node.left = None
            return make_tree(node.right, node)

        self.right = None
        make_tree(root, self)
        return self.right
