"""
Leetcode 1497
Runtime: 740 ms, faster than 20.00% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
Memory Usage: 28.1 MB, less than 56.21% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
"""


import collections


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = collections.Counter()
        for n in arr:
          	cnt[n%k] += 1
        try:
            assert cnt[0]%2 == 0
            for i in range(1, k//2+1):
                assert cnt[i] == cnt[k-i]
        except AssertionError:
            return False
        else:
            return True
