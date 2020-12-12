"""
Leetcode 1657
Leetcode weekly contest 215
Runtime: 136 ms, faster than 66.67% of Python3 online submissions for Determine if Two Strings Are Close.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Determine if Two Strings Are Close.
"""


import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        mp = collections.defaultdict(int)
        chars = set()
        for key in cnt1:
            mp[cnt1[key]] += 1
            chars.add(key)
        for key in cnt2:
            v = cnt2[key]
            if key not in chars or v not in mp:
                return False
            chars.remove(key)
            mp[v] -= 1
            if mp[v] == 0:
                del mp[v]
        return len(mp) == 0 and len(chars) == 0
