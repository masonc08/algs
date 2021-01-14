"""
Leetcode 954
O(nlogn) runtime, O(n) space
Runtime: 708 ms, faster than 55.91% of Python3 online submissions for Array of Doubled Pairs.
Memory Usage: 16.7 MB, less than 57.71% of Python3 online submissions for Array of Doubled Pairs.
"""


import collections
from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort(key=abs)
        ct = collections.Counter()
        for c in reversed(A):
            if c*2 in ct:
                ct[c*2] -= 1
                if ct[c*2] == 0:
                    del ct[c*2]
            else:
                ct[c] += 1
        return len(ct) == 0
