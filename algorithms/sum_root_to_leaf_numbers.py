"""
Leetcode 129
Runtime: 16 ms, faster than 99.87% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14.3 MB, less than 18.13% of Python3 online submissions for Sum Root to Leaf Numbers.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], cur=0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return cur*10+root.val
        return self.sumNumbers(root.left, cur*10+root.val) + self.sumNumbers(root.right, cur*10+root.val)
