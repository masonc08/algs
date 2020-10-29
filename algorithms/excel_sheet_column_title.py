"""
Leetcode 168
Runtime: 24 ms, faster than 90.78% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        sol = []
        while n:
            n -= 1
            sol.append(chr(ord('A') + n%26))
            n //= 26
        return ''.join(reversed(sol))
