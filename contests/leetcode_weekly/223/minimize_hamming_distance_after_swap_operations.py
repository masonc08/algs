"""
Leetcode 1722
Leetcode weekly contest 223
O(N+E) runtime, O(E) space
DFS solution
Runtime: 2552 ms, faster than 100.00% of Python3 online submissions for Minimize Hamming Distance After Swap Operations.
Memory Usage: 161.2 MB, less than 100.00% of Python3 online submissions for Minimize Hamming Distance After Swap Operations.
"""


import collections


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], edges: List[List[int]]) -> int:
        L = len(source)
        adj_list = [set() for _ in range(L)]
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        sol, seen = 0, [False]*L
        def dfs(node):
            if seen[node]:
                return
            seen[node] = True
            ct[source[node]] += 1
            ct[target[node]] -= 1
            for nbr in adj_list[node]:
                dfs(nbr)
        for i in range(L):
            ct = collections.Counter()
            dfs(i)
            sol += sum(v for v in ct.values() if v > 0)
        return sol
