"""
Leetcode 718
Runtime: 5420 ms, faster than 18.23% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 39 MB, less than 66.67% of Python3 online submissions for Maximum Length of Repeated Subarray.
"""


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*len(A) for _ in range(len(B))]
        sol = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i][j] += dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                    dp[i][j] += 1
                    sol = max(sol, dp[i][j])
        return sol
