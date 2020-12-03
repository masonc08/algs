"""
Leetcode 8
Runtime: 28 ms, faster than 92.55% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.2 MB, less than 17.44% of Python3 online submissions for String to Integer (atoi).
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        flip = 1
        if i >= len(s):
            return 0
        if s[i] == '-':
            flip = -1
            i += 1
        elif s[i] == '+':
            i += 1
        elif not s[i].isnumeric():
            return 0
        sol = 0
        for i in range(i, len(s)):
            if not s[i].isnumeric():
                return sol*flip
            sol *= 10
            sol += int(s[i])
            if sol*flip > 0x7fffffff:
                return 0x7fffffff
            elif sol*flip < -0x80000000:
                return -0x80000000
        return sol*flip
