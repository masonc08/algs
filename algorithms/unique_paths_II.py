"""
Leetcode 63
Runtime: 44 ms, faster than 45.31% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.4 MB, less than 23.49% of Python3 online submissions for Unique Paths II.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        for i, row in enumerate(obstacleGrid):
            for j, v in enumerate(row):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                    continue
                if v == 0:
                    if i-1 >= 0 and obstacleGrid[i-1][j] != -1:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j-1 >= 0 and obstacleGrid[i][j-1] != -1:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
                elif v == 1:
                    obstacleGrid[i][j] = -1
                else:
                    raise Exception(f"unknown value {v}")
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != -1 else 0
