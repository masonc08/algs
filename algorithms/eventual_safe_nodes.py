# Leetcode 802


class Solution:
    _memoiz = {}
    def eventualSafeNodes(self, graph):
        sol = []
        for node in range(len(graph)):
            if self._dfs(graph, node, set()):
                sol.append(node)
        return sol

    def _dfs(self, graph, node, visiting):
        if node in self._memoiz:
            return self._memoiz[node]
        if node in visiting:
            return False
        visiting.add(node)
        for neighbor in graph[node]:
            if not self._dfs(graph, neighbor, visiting):
                self._memoiz[node] = False
                return False
            self._memoiz[neighbor] = True
        visiting.remove(node)
        return True

# class Solution:
#     def eventualSafeNodes(self, graph):
#         def explore(i):
#             visited[i] = 0
#             for v in graph[i]:
#                 if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
#             visited[i] = 1
#             res.append(i)
#             return False
#         visited, res = [-1] * len(graph), []
#         for i in range(len(graph)):
#             if visited[i] == -1: explore(i)
#         return sorted(res)

print(Solution().eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))