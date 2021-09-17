"""
Leetcode 350
September Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(), nums2.sort()
        i = j = 0
        L1, L2, sol = len(nums1), len(nums2), []
        while i < L1 and j < L2:
            if nums1[i] == nums2[j]:
                sol.append(nums1[i])
                i, j = i+1, j+1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return sol
        
        
    def intersect_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ct = collections.Counter(nums1)
        sol = []
        for num in nums2:
            if not ct:
                return sol
            if num in ct:
                ct[num] -= 1
                sol.append(num)
                if ct[num] == 0:
                    del ct[num]
        return sol
