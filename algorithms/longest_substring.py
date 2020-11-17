# Given two strings, find the length of the longest substring that exists in both strings

class Solution:
    def longest_substring(self, s1: str, s2: str) -> int:
        dp = [[0]*len(s2) for _ in range(len(s1))]
        sol = 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i][j] += dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                    dp[i][j] += 1
                    sol = max(sol, dp[i][j])
        return sol

class Assert(Solution):
    def __init__(self):
        assert self.longest_substring("abcde", "defhg") == 2
        assert self.longest_substring("12321", "32147")  == 3
        assert self.longest_substring("", "") == 0

Assert()
