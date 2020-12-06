"""
Leetcode 94
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        sol, stk = [], []
        runner = root
        while runner or stk:
            while runner:
                stk.append(runner)
                runner = runner.left
            leaf = stk.pop()
            sol.append(leaf.val)
            runner = leaf.right
        return sol


    """
    Iterative
    Runtime: 32 ms, faster than 50.62% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 14.2 MB, less than 36.17% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     stk = [root]
    #     sol = []
    #     while stk:
    #         parent = stk[-1]
    #         while parent and parent.left:
    #             stk.append(parent.left)
    #             parent.left = None
    #             parent = stk[-1]
    #         leaf = stk.pop()
    #         sol.append(leaf.val)
    #         leaf.right and stk.append(leaf.right)
    #     return sol


    """
    Recursive
    Runtime: 40 ms, faster than 50.62% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 14.4 MB, less than 12.66% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     sol = []
    #     def inorder(node):
    #         if not node:
    #             return
    #         inorder(node.left)
    #         sol.append(node.val)
    #         inorder(node.right)
    #     inorder(root)
    #     return sol
