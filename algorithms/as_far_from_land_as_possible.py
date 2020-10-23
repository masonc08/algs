"""
Leetcode 1162
Runtime: 632 ms, faster than 59.04% of Python3 online submissions for As Far from Land as Possible.
Memory Usage: 15.8 MB, less than 18.20% of Python3 online submissions for As Far from Land as Possible.
"""


class Solution:
    def maxDistance(self, grid):
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i-1, j))
                    q.append((i+1, j))
                    q.append((i, j-1))
                    q.append((i, j+1))
        count = 0
        while q:
            new = []
            count += 1
            while q:
                i, j = q.pop()
                if i == -1 or i == len(grid) or j == -1 or j == len(grid) or grid[i][j] != 0:
                    continue
                grid[i][j] = count
                new.append((i-1, j))
                new.append((i+1, j))
                new.append((i, j-1))
                new.append((i, j+1))
            q = new
        return -1 if count == 1 else count-1

Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])