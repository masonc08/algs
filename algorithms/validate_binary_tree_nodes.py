"""
Leetcode 1362
Runtime: 312 ms, faster than 67.63% of Python3 online submissions for Validate Binary Tree Nodes.
Memory Usage: 16.7 MB, less than 64.42% of Python3 online submissions for Validate Binary Tree Nodes.
"""


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ns = set(range(n))
        for i in range(n):
            if i in ns:
                stk = [i]
                while stk:
                    new = []
                    while stk:
                        n = stk.pop()
                        if leftChild[n] != -1:
                            if leftChild[n] in ns and leftChild[n] != i:
                                ns.remove(leftChild[n])
                            else:
                                return False
                            leftChild[n] > i and new.append(leftChild[n])
                        if rightChild[n] != -1 and rightChild[n] != i:
                            if rightChild[n] in ns:
                                ns.remove(rightChild[n])
                            else:
                                return False
                            rightChild[n] > i and new.append(rightChild[n])
                    stk = new
        return len(ns) == 1
