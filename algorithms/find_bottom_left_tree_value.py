"""
Leetcode 513
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS
Runtime: 44 ms, faster than 66.18% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.4 MB, less than 51.84% of Python3 online submissions for Find Bottom Left Tree Value.
"""
# class Solution:
#     def findBottomLeftValue(self, root: TreeNode) -> int:
#         li = [root]
#         while li:
#             new = []
#             for node in li:
#                 new += filter(None, (node.left, node.right))
#             if not new:
#                 return li[0].val
#             li = new
#         raise Exception()


"""
DFS
Runtime: 68 ms, faster than 5.33% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 17.1 MB, less than 13.60% of Python3 online submissions for Find Bottom Left Tree Value.
"""
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node, d=0, maxd=-1, sol=0):
            if not node:
                return maxd, sol
            if not node.left and not node.right:
                if d > maxd:
                    return d, node.val
                return maxd, sol
            maxd, sol = dfs(node.left, d+1, maxd, sol)
            maxd, sol = dfs(node.right, d+1, maxd, sol)
            return maxd, sol
        _, sol = dfs(root)
        return sol
