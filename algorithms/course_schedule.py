# Leetcode 207


import collections


"""
Topological sort by BFS
O(V+E) runtime, O(V+E) space, where V=numCourses, E=prerequesites.length
Runtime: 100 ms, faster than 58.00% of Python3 online submissions for Course Schedule.
Memory Usage: 15.5 MB, less than 84.67% of Python3 online submissions for Course Schedule.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_li, indeg = [[] for _ in range(numCourses)], [0]*numCourses
        for v, u in prerequisites:
            adj_li[u].append(v)
            indeg[v] += 1
        q = collections.deque(node for node, v in enumerate(indeg) if not v)
        while q:
            node = q.popleft()
            for nbr in adj_li[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        return not any(indeg)


"""
Topological sort by DFS
O(V+E) runtime, O(V+E) space, where V=numCourses, E=prerequesites.length
Runtime: 100 ms, faster than 58.00% of Python3 online submissions for Course Schedule.
Memory Usage: 17.5 MB, less than 21.55% of Python3 online submissions for Course Schedule.
"""
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_li = [[] for _ in range(numCourses)]
#         for v, u in prerequisites:
#             adj_li[u].append(v)
#         visited = [False]*numCourses
#         def is_cycle(node, visiting):
#             if visited[node]:
#                 return False
#             if visiting[node]:
#                 return True
#             visiting[node] = True
#             for nbr in adj_li[node]:
#                 if is_cycle(nbr, visiting):
#                     return True
#             visited[node] = True
#             return False
#         return not any(is_cycle(node, [False]*numCourses) for node in range(numCourses) if not visited[node])
        

"""
Runtime: 100 ms, faster than 58.00% of Python3 online submissions for Course Schedule.
Memory Usage: 17.5 MB, less than 21.55% of Python3 online submissions for Course Schedule.
"""
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = [[]*len(numCourses)]
#         visited = [0]*len(numCourses)
#         for main, dep in prerequisites:
#             graph[main].append(dep)

#         def dfs(node):
#             if visited == -1:
#                 return False
#             if visited == 1:
#                 return True
#             visit[node] = -1
#             for adj_edge in graph[node]:
#                 if not dfs(node):
#                     return False
#             visit[node] = 1
#             return True

#         for node in range(numCourses):
#             if not dfs(node):
#                 return False
#         return True
 