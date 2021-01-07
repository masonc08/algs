"""
Leetcode 343
Runtime: 36 ms, faster than 42.82% of Python3 online submissions for Integer Break.
Memory Usage: 14.3 MB, less than 19.66% of Python3 online submissions for Integer Break.
"""


import functools


class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(None)
        def helper(n):
            if n == 0:
                return 1
            return max(i*helper(n-i) for i in range(1, n+1))
        return max(i*helper(n-i) for i in range(1, n))
