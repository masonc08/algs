"""
Leetcode 438
Runtime: 200 ms, faster than 24.35% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.2 MB, less than 22.40% of Python3 online submissions for Find All Anagrams in a String.
"""


import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ct = collections.Counter(p)
        i = j = 0
        cur = ct.copy()
        sol = []
        while i < len(s):
            c = s[i]
            if c not in cur:
                i = j = i+1
                cur = ct.copy()
                continue
            elif c in cur:
                cur[c] -= 1
            if i-j+1 == len(p):
                if all(cur[key] == 0 for key in cur):
                    sol += j,
                cur[s[j]] += 1
                j += 1
            i += 1
        return sol

