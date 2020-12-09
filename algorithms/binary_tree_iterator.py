"""
Leetcode 173
Runtime: 76 ms, faster than 56.71% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.8 MB, less than 67.90% of Python3 online submissions for Binary Search Tree Iterator.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = [root]
        self._update()


    def _update(self):
        if self.stk:
            run = self.stk[-1].left
            while run:
                self.stk.append(run)
                run = run.left


    def next(self) -> int:
        ret = self.stk.pop()
        if ret.right: 
            self.stk.append(ret.right)
            self._update()
        return ret.val
        

    def hasNext(self) -> bool:
        return bool(self.stk)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()