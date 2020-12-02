"""
Leetcode 205
Runtime: 44 ms, faster than 42.58% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.4 MB, less than 65.53% of Python3 online submissions for Isomorphic Strings.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        mapped = set()
        for i, c in enumerate(s):
            if (c in mp and mp[c] != t[i]) or (c not in mp and t[i] in mapped):
                return False
            mp[c] = t[i]
            mapped.add(t[i])
        return True
