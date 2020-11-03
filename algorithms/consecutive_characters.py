"""
Leetcode 1446
November Leetcoding Challenge
Runtime: 44 ms, faster than 54.86% of Python3 online submissions for Consecutive Characters.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Consecutive Characters.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        sol = 0
        i = 0
        while i < len(s)-1:
            tmp = 1
            if s[i] == s[i+1]:
                while i < len(s)-1 and s[i] == s[i+1]:
                    tmp += 1
                    i += 1
            sol = max(sol, tmp)
            i += 1
        return sol
