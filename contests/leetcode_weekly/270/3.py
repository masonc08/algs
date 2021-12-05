# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_path(v):
            sol = []
            def recurse(node):
                if not node:
                    return False
                if node.val == v:
                    return True
                sol.append('L')
                if recurse(node.left):
                    return True
                sol[-1] = 'R'
                if recurse(node.right):
                    return True
                sol.pop()
                return False

            recurse(root)
            return sol

        a, b = tuple(map(get_path, (startValue, destValue)))
        L1, L2 = len(a), len(b)
        i = 0
        while i < L1 and i < L2 and a[i] == b[i]:
            i += 1
        return "".join(['U']*(L1-i) + b[i:])
        
