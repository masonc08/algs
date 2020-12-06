"""
Leetcode 100
Runtime: 28 ms, faster than 79.40% of Python3 online submissions for Same Tree.
Memory Usage: 14.3 MB, less than 18.42% of Python3 online submissions for Same Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    """
    Identical tree but flipped check
    """
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     def match(p, q, rev=False):
    #         if not p and not q:
    #             return True
    #         if not p or not q or p.val != q.val:
    #             return False
    #         return match(p.left, q.right if rev else q.left) and \
    #             match(p.right, q.left if rev else q.right)

    #     return p and q and p.val == q.val and (
    #         match(p.left, q.left) and match(p.right, q.right) or \
    #             match(p.right, q.left, True) and match(p.left, q.right, True)
    #     )
