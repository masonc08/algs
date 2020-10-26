class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        depth = len(matrix)//2
        for i in range(depth):
            for j in range(i, len(matrix)-i-1):
                (
                    matrix[j][i],
                    matrix[i][len(matrix)-1-j],
                    matrix[len(matrix)-1-j][len(matrix)-1-i],
                    matrix[len(matrix)-1-i][j]
                ) = (
                    matrix[len(matrix)-1-i][j],
                    matrix[j][i],
                    matrix[i][len(matrix)-1-j],
                    matrix[len(matrix)-1-j][len(matrix)-1-i]
                )
