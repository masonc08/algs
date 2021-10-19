"""
Leetcode 496
October Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp, stk = {}, []
        for i in range(len(nums2)-1, -1, -1):
            v = nums2[i]
            while stk and stk[-1] <= v:
                stk.pop()
            mp[v] = stk[-1] if stk else -1
            stk.append(v)
        return list(map(mp.get, nums1))
