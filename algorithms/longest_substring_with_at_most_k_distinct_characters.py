"""
Leetcode 340, Daily Coding Problem #13
O(n) runtime, O(1) space
Runtime: 112 ms, faster than 18.51% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 14.2 MB, less than 96.34% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
"""


import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        ct = collections.Counter()
        i = sol = 0
        for j, c in enumerate(s):
            ct[c] += 1
            while i < j and len(ct) > k:
                c1 = s[i]
                ct[c1] -= 1
                if ct[c1] == 0:
                    del ct[c1]
                i += 1
            sol = max(j-i+1, sol)
        return sol
