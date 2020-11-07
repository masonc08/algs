"""
Leetcode 210
Runtime: 92 ms, faster than 94.68% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.4 MB, less than 8.32% of Python3 online submissions for Course Schedule II.
"""


from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stk = []
        adj_list = [set() for _ in range(numCourses)]
        indegrees = [0]*numCourses
        for v, u in prerequisites:
            adj_list[u].add(v)
            indegrees[v] += 1
        leaves = set()
        for node, deg in enumerate(indegrees):
            if deg == 0:
                leaves.add(node)
        while leaves:
            new_leaves = set()
            for leaf in leaves:
                stk.append(leaf)
                for nbr in adj_list[leaf]:
                    indegrees[nbr] -= 1
                    if indegrees[nbr] == 0:
                        new_leaves.add(nbr)
            leaves = new_leaves
        if len(stk) != numCourses:
            return []
        return stk
