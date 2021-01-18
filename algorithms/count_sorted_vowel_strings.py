"""
Leetcode 1641
January Leetcoding challenge
"""


import itertools
import math


class Solution:
    """
    O(1) runtime, O(1) space
    Combinations, (n+4)C4
    Runtime: 32 ms, faster than 69.21% of Python3 online submissions for Count Sorted Vowel Strings.
    Memory Usage: 13.9 MB, less than 98.94% of Python3 online submissions for Count Sorted Vowel Strings.
    """
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n+4, 4)

    """
    O(n) runtime, O(1) space
    DP
    Runtime: 44 ms, faster than 27.39% of Python3 online submissions for Count Sorted Vowel Strings.
    Memory Usage: 14.1 MB, less than 94.00% of Python3 online submissions for Count Sorted Vowel Strings.
    """
    # def countVowelStrings(self, n: int) -> int:
    #     dp = (0,) + (1,)*5
    #     for _ in range(n):
    #         dp = tuple(itertools.accumulate(dp))
    #     return dp[-1]