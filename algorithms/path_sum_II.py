"""
Leetcode 113
Runtime: 44 ms, faster than 71.39% of Python3 online submissions for Path Sum II.
Memory Usage: 15.7 MB, less than 48.66% of Python3 online submissions for Path Sum II.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, tar: int) -> List[List[int]]:
        path, sol = [], []
        def dfs(node, cur):
            path.append(node.val)
            new = cur+node.val
            node.left and dfs(node.left, new)
            node.right and dfs(node.right, new)
            if not node.left and not node.right and new == tar:
                sol.append(path.copy())
            path.pop()

        root and dfs(root, 0)
        return sol


"""
class Solution:
	def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
		sol = []
    path = []
    def dfs(node, cur=0):
			if not node:
				return
        cur += node.val
        path.append(node.val)
			if cur > sum:
				path.pop()
				return 
        if not node.left and not node.right:
				if cur == sum:
					sol.append(path.copy())
        path.pop()
        return
        dfs(node.left, cur)
    	dfs(node.right, cur)
        path.pop()
  
    dfs(root)
    return sol
"""