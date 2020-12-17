"""
Leetcode 542
Runtime: 868 ms, faster than 17.28% of Python3 online submissions for 01 Matrix.
Memory Usage: 16.5 MB, less than 78.75% of Python3 online submissions for 01 Matrix.
"""


class Solution:
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
 
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = -1
                else:
                    q.append((i, j))
        wave = 0
        while q:
            new = []
            while q:
                i, j  = q.pop()
                for i1, j1 in self.dirs:
                    if 0 <= i+i1 < len(matrix) and 0 <= j+j1 < len(matrix[0]) and matrix[i+i1][j+j1] == -1:
                        matrix[i+i1][j+j1] = wave+1
                        new.append((i+i1, j+j1))
            wave += 1
            q = new
        return matrix
