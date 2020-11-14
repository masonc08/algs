"""
Leetcode 458
Runtime: 28 ms, faster than 72.86% of Python3 online submissions for Poor Pigs.
Memory Usage: 13.8 MB, less than 81.43% of Python3 online submissions for Poor Pigs.
"""


import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest//minutesToDie+1
        return math.ceil(math.log(buckets, base))
