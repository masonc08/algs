"""
Leetcode 1110
Runtime: 64 ms, faster than 84.64% of Python3 online submissions for Delete Nodes And Return Forest.
Memory Usage: 14.6 MB, less than 74.09% of Python3 online submissions for Delete Nodes And Return Forest.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        to_delete.add(0)
        sol = []
        def explore(nd):
            if not nd:
                return None
            nd.left = explore(nd.left)
            if not to_delete:
                return nd
            nd.right = explore(nd.right)
            if not to_delete:
                return nd
            if nd.val in to_delete:
                to_delete.remove(nd.val)
                nd.left and sol.append(nd.left)
                nd.right and sol.append(nd.right)
                return None
            return nd
        explore(TreeNode(0, root))
        return sol
