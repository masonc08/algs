"""
Leetcode 1717
Leetcode biweekly contest 43
O(n) runtime, O(n) space
Runtime: 504 ms, faster than 33.33% of Python3 online submissions for Maximum Score From Removing Substrings.
Memory Usage: 16.1 MB, less than 33.33% of Python3 online submissions for Maximum Score From Removing Substrings.
"""


class Solution:
    def get_patterns(self, x, y):
        if x > y:
            h, l = "ab", "ba"
            hpts, lpts = x, y
        else:
            h, l = "ba", "ab"
            hpts, lpts = y, x
        return h, l, hpts, lpts

    def search(self, A, query, pts):
        sol, stk = 0, []
        for c in A:
            if stk and stk[-1] + c == query:
                stk.pop()
                sol += pts
            else:
                stk += c,
        return sol, stk

    def maximumGain(self, s: str, x: int, y: int) -> int:
        h, l, hpts, lpts = self.get_patterns(x, y)
        solH, rem = self.search(s, h, hpts)
        solL, _ = self.search(rem, l, lpts)
        return solH+solL
