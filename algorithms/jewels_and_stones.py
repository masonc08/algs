"""
Leetcode 771
Runtime: 72 ms, faster than 7.29% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.4 MB, less than 11.37% of Python3 online submissions for Jewels and Stones.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(j) for j in jewels)
