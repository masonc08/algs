"""
Leetcode 107
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
    # Runtime: 37 ms, faster than 33.35% of Python3 online submissions for Binary Tree Level Order Traversal II.
    # Memory Usage: 15.4 MB, less than 7.84% of Python3 online submissions for Binary Tree Level Order Traversal II.
    # No reversals
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def get_depth(root):
            return 1 + max(get_depth(root.left), get_depth(root.right)) if root else 0
        depth = get_depth(root)
        sol, stk = [None]*depth, [root]
        for i in range(depth-1, -1, -1):
            sol[i], cur = [node.val for node in stk], []
            for node in stk:
                node.left and cur.append(node.left)
                node.right and cur.append(node.right)
            stk = cur
        return sol
    
    # Runtime: 53 ms, faster than 15.75% of Python3 online submissions for Binary Tree Level Order Traversal II.
    # Memory Usage: 14.7 MB, less than 23.56% of Python3 online submissions for Binary Tree Level Order Traversal II.
    # def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root:
    #         return []
    #     stk, sol = [root], []
    #     while stk:
    #         sol.append([node.val for node in stk])
    #         cur = []
    #         for node in stk:
    #             if node.left:
    #                 cur.append(node.left)
    #             if node.right:
    #                 cur.append(node.right)
    #         stk = cur
    #     sol.reverse()
    #     return sol
