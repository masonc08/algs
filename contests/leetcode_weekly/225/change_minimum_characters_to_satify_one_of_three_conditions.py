"""
Leetcode 1737
O(m+n) runtime, O(1) space
Runtime: 272 ms, faster than 33.33% of Python3 online submissions for Change Minimum Characters to Satisfy One of Three Conditions.
Memory Usage: 15 MB, less than 33.33% of Python3 online submissions for Change Minimum Characters to Satisfy One of Three Conditions.
"""


import collections


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        convert = lambda x: ord(x)-97
        cta, ctb = collections.Counter(map(convert, a)), collections.Counter(map(convert, b))
        sol = m+n-max((cta+ctb).values())
        for i in range(25):
            cta[i+1], ctb[i+1] = cta[i+1]+cta[i], ctb[i+1]+ctb[i]
            sol = min(sol, m-cta[i]+ctb[i], n-ctb[i]+cta[i])
        return sol
