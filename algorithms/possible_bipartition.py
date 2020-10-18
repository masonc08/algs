"""
Leetcode 886
Runtime: 708 ms, faster than 86.10% of Python3 online submissions for Possible Bipartition.
Memory Usage: 19.7 MB, less than 9.33% of Python3 online submissions for Possible Bipartition.
"""

import collections


class Solution:
    def possibleBipartition(self, N, dislikes):
        adj_list = collections.defaultdict(list)
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()
        for node in range(1, N+1):
            if node in visited or -node in visited:
                continue
            if not self._dfs(node, adj_list, visited):
                return False
        return True

    def _dfs(self, node, adj_list, visited):
        if -node in visited:
            return False
        if node in visited:
            return True
        visited.add(node)
        for adj_node in adj_list[abs(node)]:
            if not self._dfs(adj_node if node < 0 else -adj_node, adj_list, visited):
                return False
        return True

print(Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]]))