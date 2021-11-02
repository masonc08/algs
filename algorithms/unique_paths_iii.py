"""
Leetcode 980
November Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        squares = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v in {0, 1}:
                    squares += 1
        def solve(i, j, depth):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2 and depth == squares:
                return 1
            tmp = grid[i][j]
            grid[i][j] = -1
            sol = sum((
                solve(i-1, j, depth+1),
                solve(i+1, j, depth+1),
                solve(i, j-1, depth+1),
                solve(i, j+1, depth+1)
            ))
            grid[i][j] = tmp
            return sol
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    return solve(i, j, 0)
        raise Exception("No starting square")
