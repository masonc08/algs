"""
Leetcode 1026
Runtime: 32 ms, faster than 94.34% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
Memory Usage: 19.2 MB, less than 22.53% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    _LOWER = 0
    _UPPER = 10**5

    def maxAncestorDiff(self, root: TreeNode) -> int:
        sol, _, _ = self._maxAncestorDiff(root)
        return sol

    def _maxAncestorDiff(self, root: TreeNode) -> tuple:
        if not root.left and not root.right:
            return 0, root.val, root.val
        if root.left:
            ldiff, lmin, lmax = self._maxAncestorDiff(root.left)
        if root.right:
            rdiff, rmin, rmax = self._maxAncestorDiff(root.right)
        return (
            max(
                ldiff if root.left else 0,
                rdiff if root.right else 0,
                abs(root.val-lmin) if root.left else 0,
                abs(root.val-lmax) if root.left else 0,
                abs(root.val-rmin) if root.right else 0,
                abs(root.val-rmax) if root.right else 0
            ),
            min(
                root.val,
                lmin if root.left else self._UPPER,
                rmin if root.right else self._UPPER
            ),
            max(
                root.val,
                lmax if root.left else self._LOWER,
                rmax if root.right else self._LOWER
            )
        )
