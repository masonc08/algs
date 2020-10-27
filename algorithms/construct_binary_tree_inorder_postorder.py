# Leetcode 106

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
index specification
Runtime: 60 ms, faster than 74.97% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 19.5 MB, less than 8.85% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        mp = {}
        for i, num in enumerate(inorder):
            mp[num] = i
        def _buildTree(lstart, lend, rstart, rend):
            if lstart == lend and rstart == rend:
                return None
            val = postorder[rend-1]
            pos = mp[val]
            left = _buildTree(lstart, pos, rstart, rstart+pos-lstart)
            right = _buildTree(pos+1, lend, rstart+pos-lstart, rstart-lstart+lend-1)
            return TreeNode(val, left, right)
        return _buildTree(0, len(inorder), 0, len(postorder))

"""
list splicing
Runtime: 204 ms, faster than 31.71% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 87.9 MB, less than 8.85% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""
# class Solution:
#     def buildTree(self, inorder, postorder) -> TreeNode:
#         mp = {}
#         for i, num in enumerate(inorder):
#             mp[num] = i
#         return self._buildTree(inorder, postorder, mp, 0)

#     def _buildTree(self, inorder, postorder, mp, offset):
#         if len(inorder) == 0 and len(postorder) == 0:
#             return None
#         val = postorder[-1]
#         pos = mp[val]-offset
#         left_inorder = inorder[:pos]
#         left_postorder = postorder[:pos]
#         left = self._buildTree(left_inorder, left_postorder, mp, offset)
#         right_inorder = inorder[pos+1:]
#         right_postorder = postorder[pos:-1]
#         right = self._buildTree(right_inorder, right_postorder, mp, offset+pos+1)
#         return TreeNode(val, left, right)

Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])