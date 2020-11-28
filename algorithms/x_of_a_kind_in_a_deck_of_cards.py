"""
Leetcode 914
Runtime: 136 ms, faster than 34.51% of Python3 online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 14.6 MB, less than 13.74% of Python3 online submissions for X of a Kind in a Deck of Cards.
"""


import math
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        col = collections.Counter(deck)
        return math.gcd(*[col]) != 1
