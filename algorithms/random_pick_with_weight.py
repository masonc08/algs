"""
Leetcode 528
O(n) constructor, O(logn) query, O(n) space overall
Runtime: 168 ms, faster than 95.50% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 18.6 MB, less than 90.78% of Python3 online submissions for Random Pick with Weight.
"""


import itertools
import bisect
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = list(itertools.accumulate(w, initial=0))

    def pickIndex(self) -> int:
        n = random.random()*self.w[-1]
        return bisect.bisect(self.w, n)-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()