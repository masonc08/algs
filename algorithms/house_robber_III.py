"""
Leetcode 337
Runtime: 44 ms, faster than 87.60% of Python3 online submissions for House Robber III.
Memory Usage: 16.2 MB, less than 36.25% of Python3 online submissions for House Robber III.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            left_incl, left_nincl = helper(node.left)
            right_incl, right_nincl = helper(node.right)
            return (
                left_nincl+right_nincl+node.val,
                max(left_incl, left_nincl)+max(right_incl, right_nincl)
            )

        return max(helper(root))
