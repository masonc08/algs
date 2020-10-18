"""
Leetcode 797
"""


import collections


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = collections.defaultdict(list)
        return self._dfs(0, graph, paths)

    def _dfs(self, node, graph, paths):
        if node in paths:
            return paths[node]
        if node == len(graph) - 1:
            return [[node]]
        for adj_node in graph[node]:
            paths_to_end = self._dfs(adj_node, graph, paths)
            for new_path in paths_to_end:
                paths[node].append([node] + new_path)
        return paths[node]
