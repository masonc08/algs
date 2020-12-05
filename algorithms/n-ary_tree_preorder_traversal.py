"""
Leetcode 589
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    """
    Iterative
    Runtime: 56 ms, faster than 21.18% of Python3 online submissions for N-ary Tree Preorder Traversal.
    Memory Usage: 16.1 MB, less than 15.67% of Python3 online submissions for N-ary Tree Preorder Traversal.
    """
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stk = [root]
        sol = []
        while stk:
            parent = stk.pop()
            sol.append(parent.val)
            stk += reversed(parent.children)
        return sol


    """
    Recursive
    Runtime: 48 ms, faster than 79.68% of Python3 online submissions for N-ary Tree Preorder Traversal.
    Memory Usage: 16.1 MB, less than 15.67% of Python3 online submissions for N-ary Tree Preorder Traversal.
    """
    # def preorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []
    #     sol = []
    #     def dfs(node):
    #         sol.append(node.val)
    #         for child in node.children:
    #             dfs(child)
    #     dfs(root)
    #     return sol
