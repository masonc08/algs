"""
Leetcode 424
Runtime: 160 ms, faster than 35.90% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.4 MB, less than 9.79% of Python3 online submissions for Longest Repeating Character Replacement.
"""


import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = sol = 0
        ct = collections.Counter()
        while j < len(s):
            v = s[j]
            ct[v] += 1
            most = max(ct.values())
            if j-i+1-most > k:
                ct[s[i]] -= 1
                i += 1
            sol = max(j-i+1, sol)
            j += 1
        return sol
