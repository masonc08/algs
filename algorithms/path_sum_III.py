"""
Leetcode 437
Runtime: 48 ms, faster than 81.81% of Python3 online submissions for Path Sum III.
Memory Usage: 15.8 MB, less than 24.23% of Python3 online submissions for Path Sum III.
"""


import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, k: int) -> int:
        ct = collections.Counter([0])
        def dfs(node, cur=0):
            if not node:
                return 0
            sol = 0
            cur += node.val
            sol += ct[cur-k]
            ct[cur] += 1
            sol += dfs(node.left, cur) + dfs(node.right, cur)
            ct[cur] -= 1
            return sol
        return dfs(root)

