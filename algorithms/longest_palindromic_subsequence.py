"""
Leetcode 516
Runtime: 1744 ms, faster than 43.04% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.5 MB, less than 68.49% of Python3 online submissions for Longest Palindromic Subsequence.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in s]
        for i in range(len(s)):
            for j in range(len(s)-i):
                if i == 0:
                    dp[j][j] = 1
                elif s[j] == s[j+i]:
                    dp[j][j+i] = dp[j+1][j+i-1]+2
                else:
                    dp[j][j+i] = max(dp[j][j+i-1], dp[j+1][j+i])
        return dp[0][-1]
