"""
Leetcode 637
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 44 ms, faster than 91.19% of Python3 online submissions for Average of Levels in Binary Tree.
    Memory Usage: 16.4 MB, less than 41.77% of Python3 online submissions for Average of Levels in Binary Tree.
    """
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        sol = []
        prev = [root]
        while prev:
            ttl = 0
            new = []
            for node in prev:
                ttl += node.val
                node.left and new.append(node.left)
                node.right and new.append(node.right)
            sol.append(ttl/len(prev))
            prev = new
        return sol

    """
    Runtime: 40 ms, faster than 71.82% of Python online submissions for Average of Levels in Binary Tree.
    Memory Usage: 18.3 MB, less than 21.48% of Python online submissions for Average of Levels in Binary Tree.
    """
    # def averageOfLevels(self, root):
    #     self.sums, self.nodes = [], []
    #     self._averageOfLevels(root, 0)
    #     for i in range(0, len(self.sums)):
    #         self.sums[i] /= self.nodes[i]
    #     return self.sums

    # def _averageOfLevels(self, root, level):
    #     if root:
    #         if level == len(self.sums):
    #             self.sums.append(0.0)
    #             self.nodes.append(0)
    #         self.sums[level] += root.val
    #         self.nodes[level] += 1
    #         self._averageOfLevels(root.left, level + 1)
    #         self._averageOfLevels(root.right, level + 1)
