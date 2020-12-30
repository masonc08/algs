"""
Daily Coding Problem #3, Leetcode 297
Runtime: 112 ms, faster than 80.47% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 19.1 MB, less than 27.19% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sol = []
        def dfs(node):
            if not node:
                sol.append('#')
                return
            sol.append(str(node.val))
            dfs(node.left), dfs(node.right)
        dfs(root)
        return ','.join(sol)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def build(i=0):
            if data[i] == '#':
                return None, i
            node = TreeNode(int(data[i]))
            node.left, i = build(i+1)
            node.right, i = build(i+1)
            return node, i
        sol, _ = build()
        return sol
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))