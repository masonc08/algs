"""
Leetcode 116
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

"""
Recurisve, O(n) space
Runtime: 56 ms, faster than 94.01% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.6 MB, less than 50.47% of Python3 online submissions for Populating Next Right Pointers in Each Node.
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        if root.left:
            self.connect(root.left)
        if root.right:
            self.connect(root.right)
        if root.left and root.right:
            l, r = root.left, root.right
            l.next = r
            while l.right and r.left:
                l = l.right
                r = r.left
                l.next = r
        return root


"""
Iterative, O(n) space
Runtime: 48 ms, faster than 75.51% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return root
#         old = [root]
#         while old:
#             new = []
#             for i, node in enumerate(old):
#                 if node.left:
#                     new.append(node.left)
#                 if node.right:
#                     new.append(node.right)
#                 if i+1 != len(old):
#                     node.next = old[i+1]
#             old = new
#         return root