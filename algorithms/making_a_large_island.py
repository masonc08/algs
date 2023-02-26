"""
Leetcode 827
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1))
        sizes = {}
        island_index = 2
        N, M = len(grid), len(grid[0])

        def dfs(i, j):
            if i == -1 or i == N or j == -1 or j == M or grid[i][j] != 1:
                return 0
            grid[i][j] = island_index
            return sum(dfs(i+i1, j+j1) for i1, j1 in DIRS) + 1

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    sizes[island_index] = dfs(i, j)
                    island_index += 1
        sol = max(sizes.values()) if sizes else 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    nearby_islands = set(
                        grid[i+i1][j+j1] for i1, j1 in DIRS \
                            if (i+i1 >= 0 and i+i1 < N and j+j1 >= 0 and j+j1 < M) \
                                and grid[i+i1][j+j1] != 0
                    )
                    sol = max(sol, sum(map(sizes.get, nearby_islands))+1)
        return sol
