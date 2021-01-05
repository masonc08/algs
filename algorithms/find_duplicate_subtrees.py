"""
Leetcode 952
"""


import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
"""
O(n) runtime, O(n^2) space using unique IDing system
Runtime: 60 ms, faster than 73.78% of Python3 online submissions for Find Duplicate Subtrees.
Memory Usage: 17.7 MB, less than 87.11% of Python3 online submissions for Find Duplicate Subtrees.
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ider = collections.defaultdict()
        ider.default_factory = ider.__len__
        ct = collections.Counter()
        sol = []
        def getid(node):
            if not node:
                return None
            t = ider[(node.val, getid(node.left), getid(node.right))]
            ct[t] += 1
            if ct[t] == 2:
                sol.append(node)
            return t
        getid(root)
        return sol


    """
    Runtime: 108 ms, faster than 13.47% of Python3 online submissions for Find Duplicate Subtrees.
    Memory Usage: 17.8 MB, less than 83.24% of Python3 online submissions for Find Duplicate Subtrees.
    """
#     def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
#         ct = collections.Counter()
#         sol = []
#         def tuplify(node):
#             if not node:
#                 return None
#             t = (node.val, tuplify(node.left), tuplify(node.right))
#             ct[t] += 1
#             if ct[t] == 2:
#                 sol.append(node)
#             return t
#         tuplify(root)
#         return sol
