"""
Leetcode 1457
December Leetcoding challenge
Runtime: 380 ms, faster than 80.53% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 49.4 MB, less than 78.42% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        ct = [0]*10

        def dfs(node):
            ct[node.val] += 1
            if not node.left and not node.right:
                odds = 0
                for i in range(1, 10):
                    if ct[i]%2 == 1:
                        odds += 1
                    if odds > 1:
                        break
                ct[node.val] -= 1
                return 1 if odds <= 1 else 0
            ttl = 0
            if node.left:
                ttl += dfs(node.left)
            if node.right:
                ttl += dfs(node.right)
            ct[node.val] -= 1
            return ttl
            
        return dfs(root)

