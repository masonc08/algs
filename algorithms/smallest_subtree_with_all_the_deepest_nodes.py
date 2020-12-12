"""
Leetcode 865
Leetcode 1123
December Leetcoding challenge
Runtime: 32 ms, faster than 82.62% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
Memory Usage: 14.6 MB, less than 9.02% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, d=0):
            if not node:
                return node, d
            lnode, ldepth = dfs(node.left, d+1)
            rnode, rdepth = dfs(node.right, d+1)
            if ldepth == rdepth:
                return node, ldepth
            if ldepth > rdepth:
                return lnode, ldepth
            return rnode, rdepth
        sol, _ = dfs(root)
        return sol
