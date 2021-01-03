"""
Leetcode 1376
Runtime: 2048 ms, faster than 5.01% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 68.6 MB, less than 5.88% of Python3 online submissions for Time Needed to Inform All Employees.
"""


import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = collections.defaultdict(set)
        for v, u in enumerate(manager):
            adj_list[u].add(v)
        def dfs(node):
            if not adj_list[node]:
                return 0
            return informTime[node] + max(dfs(sub) for sub in adj_list[node])
        return dfs(headID)