"""
Leetcode 64
"""


class Solution:
    """
    O(n^2) runtime, O(1) space
    Runtime: 96 ms, faster than 63.52% of Python3 online submissions for Minimum Path Sum.
    Memory Usage: 15.8 MB, less than 17.67% of Python3 online submissions for Minimum Path Sum.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(n):
                v = grid[i][j]
                if j != 0:
                    grid[i][j] = min(v+grid[i-1][j], v+grid[i][j-1])
                else:
                    grid[i][j] += grid[i-1][j]
        return grid[-1][-1]


    """
    O(n^2) runtime, O(n) space, caching 2 rows for dp
    Runtime: 108 ms, faster than 22.43% of Python3 online submissions for Minimum Path Sum.
    Memory Usage: 14.7 MB, less than 93.74% of Python3 online submissions for Minimum Path Sum.
    """
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     first, second = [0x7fffffff]*n, [0x7fffffff]*n
    #     first[0] = grid[0][0]
    #     for i, row in enumerate(grid):
    #         for j in range(len(row)):
    #             if j != n-1:
    #                 first[j+1] = min(first[j+1], first[j]+grid[i][j+1])
    #             if i != m-1:
    #                 second[j] = min(second[j], first[j]+grid[i+1][j])
    #         if i != m-1:
    #             first = second
    #             second = [0x7fffffff]*n
    #     return first[-1]
