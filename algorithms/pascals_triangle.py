"""
Leetcode 118
Runtime: 52 ms, faster than 5.80% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.3 MB, less than 25.56% of Python3 online submissions for Pascal's Triangle.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        sol = [None]*numRows
        sol[0] = [1]
        for i in range(2, numRows+1):
            cur = [1]*i
            for j in range(1, i-1):
                cur[j] = sol[i-2][j-1]+sol[i-2][j]
            sol[i-1] = cur
        return sol
