"""
Leetcode 1704
Leetcode weekly contest 221
Runtime: 36 ms, faster than 50.00% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Determine if String Halves Are Alike.
"""


import collections


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        L = len(s)
        a, b = s[:L//2].lower(), s[L//2:].lower()
        cta = collections.Counter(a)
        ctb = collections.Counter(b)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(cta[c] for c in vowels) == sum(ctb[c] for c in vowels)
