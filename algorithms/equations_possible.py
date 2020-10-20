"""
Leetcode 990
Runtime: 44 ms, faster than 84.62% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Satisfiability of Equality Equations.
"""


import collections


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        adj_list = collections.defaultdict(list)
        for equation in equations:
            if equation[1] == "=":
                a = equation[0]
                b = equation[-1]
                if a == b:
                    continue
                adj_list[a].append(b)
                adj_list[b].append(a)
        group = collections.defaultdict(lambda: float("-inf"))
        for i, node in enumerate(adj_list):
            self._dfs(node, i, adj_list, group)
        for equation in equations:
            if equation[1] == "!":
                a = equation[0]
                b = equation[-1]
                if a == b:
                    return False
                if group[a] is group[b]:
                    return False
        return True


    def _dfs(self, node, group_id, adj_list, group):
        if node in group:
            return
        group[node] = group_id
        for nei in adj_list[node]:
            self._dfs(nei, group_id, adj_list, group)



# class Solution:
#     def equationsPossible(self, equations: List[str]) -> bool:
#         mp = collections.defaultdict(set)
#         for equation in equations:
#             a = equation[0]
#             b = equation[-1]
#             if equation[1] == "=":
#                 if a == b:
#                     continue
#                 elif a in mp and b in mp:
#                     if mp[a] is not mp[b]:
#                         return False
#                 elif a in mp:
#                     mp[b] = mp[a]
#                     mp[a].add(b)
#                 elif b in mp:
#                     mp[a] = mp[b]
#                     mp[b].add(a)
#                 else:
#                     mp[a].add(a)
#                     mp[a].add(b)
#                     mp[b] = mp[a]
#         for equation in equations:
#             a = equation[0]
#             b = equation[-1]
#             if equation[1] == "!":
#                 if a == b:
#                     return False
#                 elif a in mp and b in mp:
#                     if mp[a] is mp[b]:
#                         return False
#                 elif a in mp:
#                     mp[b].add(b)
#                 elif b in mp:
#                     mp[a].add(a)
#                 else:
#                     mp[b].add(b)
#                     mp[a].add(a)
#         return True
