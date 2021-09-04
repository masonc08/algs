"""
Leetcode 834
September Leetcoding challenge
O(n) runtime, O(n+e) space, n=vertices and e=edges
Runtime: 1057 ms, faster than 40.41% of Python3 online submissions for Sum of Distances in Tree.
Memory Usage: 60.6 MB, less than 70.20% of Python3 online submissions for Sum of Distances in Tree.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(set)
        sol = [0]*n
        count = [1]*n
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        self._get_subtree_distances(0, None, sol, count, adj_list, n)
        self._convert_to_all_distances(0, None, sol, count, adj_list, n)
        return sol
    
    def _get_subtree_distances(self, node, parent, sol, count, adj_list, n):
        for child in adj_list[node]:
            if child == parent:
                continue
            self._get_subtree_distances(child, node, sol, count, adj_list, n)
            count[node] += count[child]
            sol[node] += count[child] + sol[child]
    
    def _convert_to_all_distances(self, node, parent, sol, count, adj_list, n):
        for child in adj_list[node]:
            if child == parent:
                continue
            sol[child] = sol[node] - count[child] + n - count[child]
            self._convert_to_all_distances(child, node, sol, count, adj_list, n)
