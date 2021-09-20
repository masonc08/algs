"""
Leetcode 133
Runtime: 36 ms, faster than 83.13% of Python3 online submissions for Clone Graph.
Memory Usage: 14.7 MB, less than 26.58% of Python3 online submissions for Clone Graph.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        cache = {}
        def helper(node):
            if node.val in cache:
                return cache[node.val]
            sol = Node(node.val)
            cache[node.val] = sol
            for nbr in node.neighbors:
                sol.neighbors.append(helper(nbr))
            return sol

        return helper(node)
