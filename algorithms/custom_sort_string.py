"""
Leetcode 791
Runtime: 32 ms, faster than 48.99% of Python3 online submissions for Custom Sort String.
Memory Usage: 14.1 MB, less than 40.40% of Python3 online submissions for Custom Sort String.
"""


import collections


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        if not S or not T:
            return T
        ctr = collections.Counter(T)
        sb = [None]*len(T)
        i = 0
        for c in S:
            while ctr.get(c, 0) != 0:
                sb[i] = c
                i += 1
                ctr[c] -= 1
            del ctr[c]
        if ctr:
            for key in ctr:
                while ctr.get(key, 0) != 0:
                    sb[i] = key
                    i += 1
                    ctr[key] -= 1
        return ''.join(sb)
