class Solution:
    def create_matrix(self):
        n = int(input())
        m  = int(input())
        matrix = []
        for x in range(n):
            row = []
            for y in range(m):
                value = int(input())
                row.append(value)
            matrix.append(row)
        return matrix

    def largest_island(self):
        matrix = self.create_matrix()
        print(type(matrix))
        largest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur = self._explore(i, j, matrix)
                largest = cur if cur > largest else largest
        return largest

    def _explore(self, i, j, matrix):
        if i >= len(matrix) or i < 0 or j >= len(matrix[0]) or j < 0:
            return 0
        cur = matrix[i][j]
        if cur == 0:
            return 0
        matrix[i][j] = 0
        n = self._explore(i-1, j, matrix)
        s = self._explore(i+1, j, matrix)
        w = self._explore(i, j-1, matrix)
        e = self._explore(i, j+1, matrix)
        nw = self._explore(i-1, j-1, matrix)
        ne = self._explore(i-1, j+1, matrix)
        sw = self._explore(i+1, j-1, matrix)
        se = self._explore(i+1, j+1, matrix)
        return n + s + w + e + nw + ne + sw + se + 1

print(Solution().largest_island())