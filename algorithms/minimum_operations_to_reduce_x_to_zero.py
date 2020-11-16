"""
Leetcode 1658
Leetcode weekly contest 215
"""


import math
import collections
from typing import List


class Solution:
    """
    Problem abstracted into longest subarray, modified to adapt for negative array input
    Runtime: 1168 ms, faster than 88.34% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    Memory Usage: 36.2 MB, less than 35.71% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        sol = self.longest_subarray(nums, target)
        return -1 if sol == -1 else len(nums)-sol

    def longest_subarray(self, nums, target):
        sol, cur = -math.inf, 0
        mp = { 0: -1 }  # Sum of 0 always exists before start of array at index -1
        if target == 0:  # 0 is possible solution if target is 0
            sol = 0
        for i, num in enumerate(nums):
            cur += num
            if cur-target in mp:
                sol = max(sol, i-mp[cur-target])
            mp[cur] = max(mp[cur], i) if cur in mp else i
        return -1 if sol == -math.inf else sol

    def assertions(self):
        assert self.minOperations([1, 1, 4, 2, 3], 5) == 2
        assert self.minOperations([1, 1, 2, 3, 4, 5], 0) == 0
        assert self.minOperations([-3, 1, -4, -3, 6, 4], 1) == 2  # Array sums to -1, but can get it without summing entire array
        assert self.minOperations([], 0) == 0
        assert self.minOperations([], -6) == -1

    """
    DFS attempt
    """
    # def minOperations(self, nums: List[int], x: int) -> int:
    #     cache = {}
    #     su = sum(nums)
    #     if su < x:
    #         return -1
    #     if su == x:
    #         return len(nums)
    #     def _minOperations(i, j, count, cur):
    #         if cur == x:
    #             return count
    #         if i == j or cur > x: 
    #             return -1
    #         if cur+nums[i] > x and cur+nums[j] > x:
    #             return -1
    #         decisions = sorted([('i', nums[i]), ('j', nums[j])], key=lambda x: x[1])
    #         # If i has the higher one
    #         if decisions[1][0] == 'i':
    #             if (i+1, j, count+1, cur+decisions[1][1]) in cache:
    #                 sol = cache[(i+1, j, count+1, cur+decisions[1][1])]
    #             else:
    #                 sol = _minOperations(i+1, j, count+1, cur+decisions[1][1])
    #                 cache[(i+1, j, count+1, cur+decisions[1][1])] = sol
    #             if sol != -1:
    #                 return sol
    #             if (i, j-1, count+1, cur+decisions[0][1]) in cache:
    #                 sol = cache[(i, j-1, count+1, cur+decisions[0][1])]
    #             else:
    #                 sol = _minOperations(i, j-1, count+1, cur+decisions[0][1])
    #                 cache[(i, j-1, count+1, cur+decisions[0][1])] = sol
    #             if sol != -1:
    #                 return sol
    #         else:
    #             if (i, j-1, count+1, cur+decisions[1][1]) in cache:
    #                 sol = cache[(i, j-1, count+1, cur+decisions[1][1])]
    #             else:
    #                 sol = _minOperations(i, j-1, count+1, cur+decisions[1][1])
    #                 cache[(i, j-1, count+1, cur+decisions[1][1])] = sol
    #             if sol != -1:
    #                 return sol
    #             if (i+1, j, count+1, cur+decisions[0][1]) in cache:
    #                 sol = cache[(i+1, j, count+1, cur+decisions[0][1])]
    #             else:
    #                 sol = _minOperations(i+1, j, count+1, cur+decisions[0][1])
    #                 cache[(i+1, j, count+1, cur+decisions[0][1])] = sol
    #             if sol != -1:
    #                 return sol
    #         return -1
    #     return _minOperations(0, len(nums)-1, 0, 0)

Solution().assertions()