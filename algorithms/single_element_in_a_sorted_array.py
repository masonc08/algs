"""
Leetcode 540
November Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L = len(nums)
        i, j = 0, L-1
        while i <= j:
            m = (i+j)//2
            v = nums[m]
            if nums[m-1:m+2].count(v) != 2:
                return v
            if m%2 == 0 and m != 0 and nums[m-1] == v or m%2 == 1 and m != L-1 and nums[m+1] == v:
                j = m-1
            else:
                i = m+1
        raise Exception()

