"""
Leetcode 785
Runtime: 168 ms, faster than 76.60% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 14.8 MB, less than 13.42% of Python3 online submissions for Is Graph Bipartite?.
"""


import collections


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        red, black = set(), set()
        def dfs(node, flip):
            if flip == 1:
                if node in black:
                    return False
                if node in red:
                    return True
                red.add(node)
            else:
                if node in red:
                    return False
                if node in black:
                    return True
                black.add(node)
            for nbr in graph[node]:
                if not dfs(nbr, -flip):
                    return False
            return True
        for i in range(len(graph)):
            if i in black or i in red:
                continue
            if not dfs(i, 1):
                return False
        return True