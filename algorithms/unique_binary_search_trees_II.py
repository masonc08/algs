"""
Leetcode 95
Runtime: 52 ms, faster than 91.31% of Python3 online submissions for Unique Binary Search Trees II.
Memory Usage: 15.7 MB, less than 47.52% of Python3 online submissions for Unique Binary Search Trees II.
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, e: int, s=1) -> List[TreeNode]:
        if e == 0:
            return []

        def helper(e, s):
            if s >= e:
                return [ TreeNode(s) if s == e else None ]
            sol = []
            for i in range(s, e+1):
                l, r = helper(i-1, s), helper(e, i+1)
                for ln in l:
                    for rn in r:
                        sol += TreeNode(i, ln, rn),
            return sol

        return helper(e, s)


        # sol = []

        # def deep_clone(node):
        #     if not node:
        #         return None
        #     cl = TreeNode(node.val)
        #     cl.left, cl.right = deep_clone(node.left), deep_clone(node.right)
        #     return cl

        # def generate(s, e, top):
        #     if s > e:
        #         return
        #     for i in range(s, e+1):
        #         top.left = generate(s, i-1, top)
        #         top.right = generate(i+1, e, top)
        #         sol.append(deep_clone(top))

        # for i in range(1, n+1):
        #     top = TreeNode(i)
        #     top.left = generate(1, i-1, top)
        #     top.right = generate(i+1, n, top)
        #     sol += deep_clone(top),
        # return sol

print(Solution().generateTrees(0))