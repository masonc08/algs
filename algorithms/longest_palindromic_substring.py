"""
Leetcode 5
Runtime: 960 ms, faster than 67.45% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.4 MB, less than 33.97% of Python3 online submissions for Longest Palindromic Substring.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        sol = (0, 0)
        for i in range(1, len(s)):
            a, b = i-1, i+1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            sol = max(sol, (a+1, b), key=lambda x: x[1]-x[0])
            if s[i] == s[i-1]:
                a, b = i-2, i+1
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                sol = max(sol, (a+1, b), key=lambda x: x[1]-x[0])
        return s[sol[0]:sol[1]]
