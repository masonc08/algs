"""
Leetcode 1011

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ttl = sum(weights)
        def can_fit(capacity):
            cur, containers = 0, 1
            for weight in weights:
                if cur+weight > capacity:
                    cur = 0
                    containers += 1
                cur += weight
                if containers > days:
                    return False
            return True

        i, j = max(math.ceil(ttl/days), max(weights)), ttl
        while i < j:
            capacity = (i+j)//2
            if can_fit(capacity):
                j = capacity
            else:
                i = capacity+1
        return i
