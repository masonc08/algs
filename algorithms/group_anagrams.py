"""
Leetcode 49
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def tupleize(s):
            sol = [0]*26
            for c in s:
                sol[ord(c)-ord('a')] += 1
            return tuple(sol)

        mp = collections.defaultdict(list)
        for s in strs:
            tup = tupleize(s)
            mp[tup].append(s)
        return mp.values()
