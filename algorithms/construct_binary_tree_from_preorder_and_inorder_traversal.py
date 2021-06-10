"""
Leetcode 105
June Leetcoding challenge
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        rootValue = preorder[0]
        sol = TreeNode(rootValue)
        idx = inorder.index(rootValue)
        leftChild = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        rightChild = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        sol.left = leftChild
        sol.right = rightChild
        return sol
