"""
Given a binary tree root where each node contains a digit from 0-9, return whether its in-order traversal is a palindrome.
Bonus: solve in O(h) space where h is height of the tree.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class InorderIterator:
    def __init__(self, root, normal=True):
        self.normal = normal
        self.stk = [root] if root else []
        self._update()
    
    def _update(self):
        node = self.stk.pop()
        while node:
            self.stk.append(node)
            node = node.left if self.normal else node.right
    
    def has_next(self):
        return len(self.stk) != 0

    def get_next(self):
        if not self.has_next():
            raise Exception("No more nodes")
        sol = self.stk.pop()
        if self.normal and sol.right:
            self.stk.append(sol.right)
            self._update()
        elif not self.normal and sol.left:
            self.stk.append(sol.left)
            self._update()
        return sol.val
        

class Solution:
    def solve(self, root):
        inorder, reverse_inorder = InorderIterator(root), InorderIterator(root, False)
        while inorder.has_next() and reverse_inorder.has_next():
            if inorder.get_next() != reverse_inorder.get_next():
                return False
        return True
