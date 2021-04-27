"""
Leetcode 326
April Leetcoding challenge
Runtime: 80 ms, faster than 53.03% of Python3 online submissions for Power of Three.
Memory Usage: 14.4 MB, less than 13.85% of Python3 online submissions for Power of Three.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19%n == 0

