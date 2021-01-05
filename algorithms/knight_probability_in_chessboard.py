"""
Leetcode 688
Runtime: 264 ms, faster than 29.69% of Python3 online submissions for Knight Probability in Chessboard.
Memory Usage: 14.5 MB, less than 58.79% of Python3 online submissions for Knight Probability in Chessboard.
"""




class Solution:
    LOCS = ((1, 2), (-1, 2), (2, 1), (-2, 1), (2, -1), (-2, -1), (-1, -2), (1, -2))
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        pre = [[0]*N for _ in range(N)]
        pre[r][c] = 1
        for _ in range(K):
            new = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    new[i][j] = sum(pre[i+i1][j+j1] for i1, j1 in self.LOCS if 0 <= i+i1 < N and 0 <= j+j1 < N) / 8
            pre = new
        return sum(sum(row) for row in pre)
