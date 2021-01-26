"""
Leetcode 314
O(N) runtime and space
Runtime: 36 ms, faster than 57.76% of Python3 online submissions for Binary Tree Vertical Order Traversal.
Memory Usage: 14.3 MB, less than 39.54% of Python3 online submissions for Binary Tree Vertical Order Traversal.
"""


import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        mp = collections.defaultdict(list)
        sol = collections.deque()
        q = collections.deque(((0, root),))
        mp[0].append(root.val)
        sol.append(mp[0])
        while q:
            col, node = q.popleft()
            if node.left:
                if col-1 not in mp:
                    sol.appendleft(mp[col-1])
                mp[col-1].append(node.left.val)
                q.append((col-1, node.left))
            if node.right:
                if col+1 not in mp:
                    sol.append(mp[col+1])
                mp[col+1].append(node.right.val)
                q.append((col+1, node.right))
        return sol
