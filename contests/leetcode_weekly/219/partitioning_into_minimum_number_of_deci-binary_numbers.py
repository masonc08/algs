"""
Leetcode 1689
Leetcode weekly contest 219
Runtime: 120 ms, faster than 25.00% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 14.8 MB, less than 25.00% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n, key=int)
