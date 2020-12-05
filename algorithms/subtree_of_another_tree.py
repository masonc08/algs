"""
Leetcode 572
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    O(S+K) runtime and space by tree serialization
    Runtime: 60 ms, faster than 99.30% of Python3 online submissions for Subtree of Another Tree.
    Memory Usage: 15.7 MB, less than 6.92% of Python3 online submissions for Subtree of Another Tree.
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverse(node):
            if not node:
                sb.append('nil')
                return
            sb.append(f'#{node.val}')
            traverse(node.left)
            traverse(node.right)

        sb = []
        traverse(s)
        s = ' '.join(sb)
        sb = []
        traverse(t)
        t = ' '.join(sb)
        return t in s


    """
    O(S*K) runtime, O(lg(S)) space by brute force
    Runtime: 284 ms, faster than 12.37% of Python3 online submissions for Subtree of Another Tree.
    Memory Usage: 15.1 MB, less than 35.96% of Python3 online submissions for Subtree of Another Tree.
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self._check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def _check(self, s, t):
        if not s and not t:
            return True
        if bool(s) ^ bool(t):
            return False
        if s.val != t.val:
            return False
        return self._check(s.left, t.left) and self._check(s.right, t.right)
