"""
Leetcode 1742
Leetcode weekly contest 226
O(n) runtime and space
Runtime: 608 ms, faster than 40.00% of Python3 online submissions for Maximum Number of Balls in a Box.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balls in a Box.
"""


import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        bins = collections.defaultdict(int)
        for ball in range(lowLimit, highLimit+1):
            key = 0
            for c in str(ball):
                key += int(c)
            bins[key] += 1
        return max(bins.values())
