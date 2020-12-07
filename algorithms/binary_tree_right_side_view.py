"""
Leetcode 199
Runtime: 40 ms, faster than 22.92% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 14.4 MB, less than 15.94% of Python3 online submissions for Binary Tree Right Side View.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        sol = []
        def dfs(node, depth=0):
            if not node:
                return
            if len(sol) == depth:
                sol.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root)
        return sol
