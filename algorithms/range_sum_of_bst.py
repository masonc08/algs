"""
Leetcode 938
November Leetcoding challenge
Runtime: 212 ms, faster than 69.98% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.2 MB, less than 7.30% of Python3 online submissions for Range Sum of BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        sol = 0
        if root.val > low:
            sol += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            sol += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            sol += root.val     
        return sol
        