"""
Leetcode 819
Runtime: 48 ms, faster than 7.68% of Python3 online submissions for Most Common Word.
Memory Usage: 14.4 MB, less than 40.52% of Python3 online submissions for Most Common Word.
"""


import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        W = [s.lower() for s in re.findall(r"\w+", paragraph)]
        ct = collections.Counter(W)
        for w in banned:
            del ct[w]
        return max(ct, key=ct.get)
