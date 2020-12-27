"""
Leetcode 1706
Leetcode weekly contest 1706
Runtime: 212 ms, faster than 100.00% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Where Will the Ball Fall.
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        up = [i for i in range(n)]
        for i in range(m-1, -1, -1):
            new_up = [0]*n
            for j in range(n):
                if grid[i][j] == 1:
                    if j == n-1 or grid[i][j+1] == -1:
                        new_up[j] = -1
                    else:
                        new_up[j] = up[j+1]
                else:
                    if j == 0 or grid[i][j-1] == 1:
                        new_up[j] = -1
                    else:
                        new_up[j] = up[j-1]
            up = new_up
        return up
