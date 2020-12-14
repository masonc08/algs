"""
Leetcode 120
# Runtime: 64 ms, faster than 24.98% of Python3 online submissions for Triangle.
# Memory Usage: 15 MB, less than 31.32% of Python3 online submissions for Triangle.
"""



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            row = triangle[i]
            for j in range(len(row)):
                row[j] = row[j]+min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
