"""
Leetcode 1745
Leetcode weekly contest 226
O(n^2) runtime and space
Runtime: 5404 ms, faster than 100.00% of Python3 online submissions for Palindrome Partitioning IV.
Memory Usage: 45.5 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning IV.
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        L = len(s)
        dp = [[False]*L for _ in range(L)]
        for i in range(L):
            for j in range(L-i):
                a, b = j, j+i
                if s[a] == s[b]:
                    if b-a+1 in {1, 2}:
                        dp[a][b] = True
                    else:
                        dp[a][b] = dp[a+1][b-1]
        return any(dp[0][i-1] and dp[i][j] and dp[j+1][-1] \
            for i in range(L-1) for j in range(i+1, L-1))
