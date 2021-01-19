# Leetcode 207

import collections


"""
Iterative DFS
O(nlogn) runtime, O(n) space
"""
class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]


"""
O(n^2) runtime, O(n) space
DFS
Runtime: 120 ms, faster than 14.76% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 14.9 MB, less than 42.17% of Python3 online submissions for Reconstruct Itinerary.
"""
# class Solution:
#     def findItinerary(self, tk: List[List[str]]) -> List[str]:
#         adj_li = collections.defaultdict(list)
#         ct = collections.Counter()
#         for u, v in tk:
#             adj_li[u] += v,
#             ct[(u, v)] += 1
#         for li in adj_li.values():
#             li.sort(reverse=True)
#         sol = []
#         def dfs(node):
#             sol.append(node)
#             if not ct:
#                 return True
#             if not adj_li[node]:
#                 sol.pop()
#                 return False
#             for nbr in reversed(adj_li[node]):
#                 ticket = (node, nbr)
#                 if ticket not in ct:
#                     continue
#                 ct[ticket] -= 1
#                 if ct[ticket] == 0:
#                     del ct[(node, nbr)]
#                 if dfs(nbr):
#                     return True
#                 ct[ticket] += 1
#             sol.pop()
#             return False
#         dfs('JFK')
#         return sol


Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])