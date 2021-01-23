"""
Leetcode 161
January Leetcoding challenge
O(n) runtime, O(1) space
Runtime: 32 ms, faster than 72.71% of Python3 online submissions for One Edit Distance.
Memory Usage: 14.4 MB, less than 19.47% of Python3 online submissions for One Edit Distance.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        Ls, Lt = len(s), len(t)
        if abs(Lt-Ls) > 1:
            return False
        i, j, editted = 0, 0, False
        while i < Ls or j < Lt:
            if (i == Ls) ^ (j == Lt):
                return not editted
            cs, ct = s[i], t[j]
            if cs != ct:
                if editted:
                    return False
                if Ls+1 == Lt:
                    j += 1
                elif Ls == Lt+1:
                    i += 1
                else:
                    i, j = i+1, j+1
                editted = True
            else:
                i, j = i+1, j+1
        return i == Ls and j == Lt and editted
        