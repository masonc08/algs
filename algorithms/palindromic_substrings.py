"""
Leetcode 647
Runtime: 108 ms, faster than 92.11% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.4 MB, less than 41.64% of Python3 online submissions for Palindromic Substrings.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        sol = 0
        for i in range(L):
            sol += self.num_of_palindromes(i, i, s) + \
                self.num_of_palindromes(i, i+1, s)
        return sol

    def num_of_palindromes(self, i, j, s):
        L = len(s)
        sol = 0
        while i >= 0 and j < L and s[i] == s[j]:
            sol, i, j = sol+1, i-1, j+1
        return sol
