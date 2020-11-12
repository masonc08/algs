"""
Leetcode 1647
Leetcode weekly contest 214
Runtime: 116 ms, faster than 86.25% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
Memory Usage: 14.8 MB, less than 99.94% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
"""

import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = collections.Counter(s)
        used_cnt = set()
        sol = 0
        for c, freq in cnt.items():
            while freq > 0 and freq in used_cnt:
                freq -=1
                sol += 1
            used_cnt.add(freq)
        return sol
