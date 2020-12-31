"""
Leetcode 1143
Runtime: 344 ms, faster than 93.42% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 14.2 MB, less than 94.26% of Python3 online submissions for Longest Common Subsequence.
"""


class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        m = len(A)
        sol = [0]*m
        for b in B:
            new = [0]*m
            for j, a in enumerate(A):
                if a == b:
                    new[j] += 1
                    if j != 0:
                        new[j] += sol[j-1]
                else:
                    tmp = sol[j]
                    if j != 0:
                        tmp = max(tmp, new[j-1])
                    new[j] += tmp
            sol = new
        return sol[-1]
