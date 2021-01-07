"""
Leetcode 515
Runtime: 80 ms, faster than 5.23% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.4 MB, less than 72.38% of Python3 online submissions for Find Largest Value in Each Tree Row.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stk = [root]
        sol = []
        while stk:
            new = []
            cur = float('-inf')
            while stk:
                node = stk.pop()
                cur = max(cur, node.val)
                new += filter(None, (node.left, node.right))
            sol += cur,
            stk = new
        return sol
