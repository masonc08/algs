import collections


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = collections.defaultdict(lambda: collections.defaultdict(int))
        for u, v, w in edgeList:
            adj_list[u][v] = min(adj_list[u][v], w)
            adj_list[v][u] = min(adj_list[v][u], w)

        cache = {}
        def search_min(u, v, cur=float('inf')):
            if (u, v) in cache:
                return cache[(u, v)]
            if v == u:
                return 0
            for neib in adj_list[u]:
                cur = min(cur, max(search_min(neib, v), adj_list[u][neib]))
            cache[(u, v)] = cur
            return cur

        sol = []
        for u, v, minw in queries:
            sol += (search_min(u, v) < minw),
        return sol
