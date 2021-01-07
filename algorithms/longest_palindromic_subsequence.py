"""
Leetcode 516
Runtime: 1744 ms, faster than 43.04% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.5 MB, less than 68.49% of Python3 online submissions for Longest Palindromic Subsequence.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        L = len(s)
        cache = [[None]*L for _ in range(L)]
        def f(i=0, j=L-1):
            if cache[i][j] is not None:
                return cache[i][j]
            if i == j:
                return 1
            if i > j:
                return 0
            sol = 0
            if s[i] == s[j]:
                sol = 2+f(i+1, j-1)
            else:
                sol = max(f(i+1, j), f(i, j-1))
            cache[i][j] = sol
            return sol
        return f()

# class solution:
#     def longestpalindromesubseq(self, s: str) -> int:
#         dp = [[0]*len(s) for _ in s]
#         for i in range(len(s)):
#             for j in range(len(s)-i):
#                 if i == 0:
#                     dp[j][j] = 1
#                 elif s[j] == s[j+i]:
#                     dp[j][j+i] = dp[j+1][j+i-1]+2
#                 else:
#                     dp[j][j+i] = max(dp[j][j+i-1], dp[j+1][j+i])
#         return dp[0][-1]
