"""
Leetcode 242
Runtime: 56 ms, faster than 24.02% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 31.57% of Python3 online submissions for Valid Anagram.
"""


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = collections.Counter(s)
        for c in t:
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            else:
                return False
        return True
