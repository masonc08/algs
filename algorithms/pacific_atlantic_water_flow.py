"""
Leetcode 417
Runtime: 272 ms, faster than 80.20% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.7 MB, less than 19.86% of Python3 online submissions for Pacific Atlantic Water Flow.
"""


import collections


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        pac, atl = [[False]*len(matrix[0]) for _ in range(len(matrix))], \
            [[False]*len(matrix[0]) for _ in range(len(matrix))]
        pacq, atlq = collections.deque(), collections.deque()
        for i in range(len(pac)):
            pacq.append((i, 0))
            atlq.append((i, len(matrix[0])-1))
            pac[i][0] = True
            atl[i][-1] = True
        for j in range(len(pac[0])):
            pacq.append((0, j))
            atlq.append((len(matrix)-1, j))
            pac[0][j] = True
            atl[-1][j] = True
        while pacq or atlq:
            if pacq:
                i, j = pacq.popleft()
                self._mutate_surroundings(i, j, matrix, pac, pacq)
            if atlq:
                i, j = atlq.popleft()
                self._mutate_surroundings(i, j, matrix, atl, atlq)
        sol = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if atl[i][j] and pac[i][j]:
                    sol.append([i, j])
        return sol


    def _mutate_surroundings(self, i, j, matrix, dp, q):
        v = matrix[i][j]
        n = matrix[i-1][j] if i != 0 else -1
        w = matrix[i][j-1] if j != 0 else -1
        s = matrix[i+1][j] if i+1 != len(matrix) else -1
        e = matrix[i][j+1] if j+1 != len(matrix[0]) else -1
        if n >= v and not dp[i-1][j]:
            dp[i-1][j] = True
            q.append((i-1, j))
        if w >= v and not dp[i][j-1]:
            dp[i][j-1] = True
            q.append((i, j-1))
        if s >= v and not dp[i+1][j]:
            dp[i+1][j] = True
            q.append((i+1, j))
        if e >= v and not dp[i][j+1]:
            dp[i][j+1] = True
            q.append((i, j+1))
