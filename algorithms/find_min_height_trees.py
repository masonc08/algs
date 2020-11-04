"""
Leetcode 310
Runtime: 244 ms, faster than 78.20% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 19.2 MB, less than 5.12% of Python3 online submissions for Minimum Height Trees.
"""


import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = collections.defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        leaves = set()
        for key in adj_list:
            if len(adj_list[key]) == 1:
                leaves.add(key)
        while len(adj_list) > 2:
            new_leaves = set()
            for leaf in leaves:
                parent = adj_list[leaf].pop()
                adj_list[parent].remove(leaf)
                del adj_list[leaf]
                if len(adj_list[parent]) == 1:
                    new_leaves.add(parent)
            leaves = new_leaves
        return leaves
