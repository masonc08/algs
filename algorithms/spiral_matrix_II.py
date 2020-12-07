"""
Leetcode 59
Runtime: 68 ms, faster than 7.04% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14.1 MB, less than 51.38% of Python3 online submissions for Spiral Matrix II.
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        sol = [[0]*n for _ in range(n)]
        i = j = 0
        cur = 1
        for l in range(n, 1, -2):
            for _ in range(l-1):
                sol[i][j] = cur
                cur += 1
                j += 1
            for _ in range(l-1):
                sol[i][j] = cur
                cur += 1
                i += 1
            for _ in range(l-1):
                sol[i][j] = cur
                cur += 1
                j -= 1
            for _ in range(l-1):
                sol[i][j] = cur
                cur += 1
                i -= 1
            i += 1
            j += 1
        if sol[i][j] == 0:
            sol[i][j] = cur
        return sol
