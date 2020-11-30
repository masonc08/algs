"""
Leetcode 171
Runtime: 24 ms, faster than 95.29% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.3 MB, less than 12.15% of Python3 online submissions for Excel Sheet Column Number.
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        sol = 0
        for c in s:
            sol *= 26
            sol += (ord(c)-ord('a')+1)
        return sol
