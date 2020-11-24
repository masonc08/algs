"""
Leetcode 58
Runtime: 32 ms, faster than 36.23% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.4 MB, less than 5.33% of Python3 online submissions for Length of Last Word.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sol = 0
        for i in range(len(s)-1, -1, -1):
            v = s[i]
            if v == ' ' and sol != 0:
                return sol
            if v != ' ':
                sol += 1
        return sol
                