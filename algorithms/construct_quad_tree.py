"""
Leetcode 427
Runtime: 132 ms, faster than 40.90% of Python3 online submissions for Construct Quad Tree.
Memory Usage: 15.1 MB, less than 32.43% of Python3 online submissions for Construct Quad Tree.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]], i1=0, j1=0, i2=None, j2=None) -> 'Node':
        i2, j2 = len(grid) if i2 is None else i2, len(grid[0]) if j2 is None else j2
        if i2-i1 == 1 and j2-j1 == 1:
            return Node(grid[i1][j1], True, None, None, None, None)
        midi, midj = (i1+i2)//2, (j1+j2)//2
        tl, tr = self.construct(grid, i1, j1, midi, midj), self.construct(grid, i1, midj, midi, j2)
        bl, br = self.construct(grid, midi, j1, i2, midj), self.construct(grid, midi, midj, i2, j2)
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True, None, None, None, None)
        return Node(0, False, tl, tr, bl, br)
