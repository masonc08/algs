"""
Leetcode 547
Runtime: 184 ms, faster than 77.07% of Python3 online submissions for Number of Provinces.
Memory Usage: 15.3 MB, less than 14.13% of Python3 online submissions for Number of Provinces.
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        sol = 0
        m = len(isConnected)
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i, nbr in enumerate(isConnected[node]):
                if nbr == 1:
                    dfs(i)
        for i in range(m):
            if i not in visited:
                dfs(i)
                sol += 1
        return sol
