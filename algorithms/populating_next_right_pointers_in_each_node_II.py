"""
Leetcode 117
Runtime: 48 ms, faster than 75.51% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
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
Runtime: 44 ms, faster than 90.92% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        sol = root
        while root:
            next_node = None
            last = self
            while root:
                if not next_node:
                    next_node = root.left or root.right 
                if root.left:
                    last.next = root.left
                    last = root.left
                if root.right:
                    last.next = root.right
                    last = root.right
                root = root.next
            root = next_node
        return sol


"""
Iterative, O(n) space
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