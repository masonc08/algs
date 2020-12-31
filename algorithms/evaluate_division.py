"""
Leetcode 399
Runtime: 32 ms, faster than 61.37% of Python3 online submissions for Evaluate Division.
Memory Usage: 14.2 MB, less than 56.26% of Python3 online submissions for Evaluate Division.
"""


import collections
import itertools


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mp = collections.defaultdict(dict)
        for (a, b), w in zip(equations, values):
            mp[a][a] = mp[b][b] = 1.0
            mp[a][b] = w
            mp[b][a] = 1/w
        for w, u, v in itertools.permutations(mp, 3):
            if w in mp[u] and v in mp[w]:
                mp[u][v] = mp[u][w]*mp[w][v]
        return [ mp[a].get(b, -1.0) for a, b in queries]
        