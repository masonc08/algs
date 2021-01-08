"""
Leetcode 657
Runtime: 68 ms, faster than 34.42% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 14.1 MB, less than 96.55% of Python3 online submissions for Robot Return to Origin.
"""


import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        f = lambda c: moves.count(c)
        return f('D') == f('U') and f('L') == f('R')
