"""
Leetcode 118
Runtime: 32 ms, faster than 54.00% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.4 MB, less than 10.02% of Python3 online submissions for Pascal's Triangle.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows+1):
            for j in range(1, i-1):
                sol[i-1][j] = sol[i-2][j-1]+sol[i-2][j]
        return sol
