"""
Leetcode 0
January Leetcoding challenge
Runtime: 624 ms, faster than 62.57% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
Memory Usage: 24.2 MB, less than 44.08% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is target:
            return cloned
        if not original:
            return None
        l = self.getTargetCopy(original.left, cloned.left, target)
        if l:
            return l
        r = self.getTargetCopy(original.right, cloned.right, target)
        if r:
            return r
        return None
