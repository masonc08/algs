"""
Leetcode 1663
Leetcode contest 216
Runtime: 924 ms, faster than 28.57% of Python3 online submissions for Smallest String With A Given Numeric Value.
Memory Usage: 15.5 MB, less than 28.57% of Python3 online submissions for Smallest String With A Given Numeric Value.
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        sol = ['a']*n
        k -= len(sol)
        i = len(sol)-1
        while k and i >= 0:
            if k >= self._get_val('z')-1:
                sol[i] = 'z'
                k -= self._get_val('z')-1
            else:
                sol[i] = self._get_char(k+1)
                k = 0
            i -= 1
        return ''.join(sol)

    def _get_val(self, c: str) -> int:
        return ord(c) - ord('a') + 1

    def _get_char(self, i: int) -> str:
        return chr(i+ord('a')-1)
