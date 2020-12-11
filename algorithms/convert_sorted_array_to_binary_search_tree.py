"""
Leetcode 108
Runtime: 64 ms, faster than 94.80% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.5 MB, less than 24.11% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int], s=None, e=None) -> TreeNode:
        if s is None and e is None:
            s, e = 0, len(nums)-1
        if s == e:
            return TreeNode(nums[s])
        if s > e:
            return None
        m = (s+e)//2
        node = TreeNode(nums[m])
        node.left = self.sortedArrayToBST(nums, s, m-1)
        node.right = self.sortedArrayToBST(nums, m+1, e)
        return node
        