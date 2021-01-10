"""
Daily Coding Problem #13
"""


import collections


class Solution:
    def longestKDistinct(self, s, k):
        ct = collections.Counter()
        i = sol = 0
        for j, c in enumerate(s):
            ct[c] += 1
            while i < j and len(ct) > k:
                ct[i] -= 1
                if ct[i] == 0:
                    del ct[i]
                i += 1
            sol = max(j-i+1, sol)
        return sol
