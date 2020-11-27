"""
Leetcode 395
Novemeber Leetcoding challenge
Runtime: 44 ms, faster than 47.35% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 14.6 MB, less than 12.57% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
"""


import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        ct = collections.Counter(s)
        for key in ct:
            if ct[key] < k:
                return max([self.longestSubstring(sbstr, k) for sbstr in s.split(key)])
        return len(s)
