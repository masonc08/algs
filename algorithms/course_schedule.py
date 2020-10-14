class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[]*len(numCourses)]
        visited = [0]*len(numCourses)
        for main, dep in prerequisites:
            graph[main].append(dep)

        def dfs(node):
            if visited == -1:
                return False
            if visited == 1:
                return True
            visit[node] = -1
            for adj_edge in graph[node]:
                if not dfs(node):
                    return False
            visit[node] = 1
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
 