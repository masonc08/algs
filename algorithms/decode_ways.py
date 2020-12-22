"""
Leetcode 91
Runtime: 28 ms, faster than 86.00% of Python3 online submissions for Decode Ways.
Memory Usage: 14.1 MB, less than 66.22% of Python3 online submissions for Decode Ways.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0:
            return 0
        if len(s) == 1:
            return 1
        pprev = prev = 1
        for i in range(1, len(s)):
            n = int(s[i]) + int(s[i-1])*10
            tmp = 0
            if 10 <= n <= 26:
                tmp += pprev
            if int(s[i]) != 0:
                tmp += prev
            pprev, prev = prev, tmp
        return prev
