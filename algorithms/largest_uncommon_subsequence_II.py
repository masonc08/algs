"""
Leetcode 522
Runtime: 32 ms, faster than 88.75% of Python3 online submissions for Longest Uncommon Subsequence II.
Memory Usage: 14.1 MB, less than 5.00% of Python3 online submissions for Longest Uncommon Subsequence II.
"""


import collections


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: -len(s))
        seen = set()
        dupes = set()
        for s in strs:
            if s in seen:
                dupes.add(s)
            else:
                seen.add(s)
        for i, s in enumerate(strs):
            if s not in dupes:
                if i == 0:
                    return len(strs[0])
                mp = collections.defaultdict(bool)
                for j in range(i):
                    a, b = strs[j], s
                    if a in mp:
                        break
                    if len(a) == len(b):
                        return len(b)
                    if self._is_subsequence(a, b):
                        mp[j] = True
                        break
                    if j == i-1:
                        return len(strs[i])
        return -1

    def _is_subsequence(self, longstr, shortstr):
        i, j = 0, 0
        while i < len(longstr) and j < len(shortstr):
            if longstr[i] == shortstr[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(shortstr)

"""
1. Sort in decreasing length
2. Identify duplicates
3. Iterate through all strings, for every string, check if it is a subsequence of 
    the strings that come before it, provided they are DIFFERENT lengths
"""