"""
Leetcode 494

"""


import functools
import collections


class Solution:
    """
    O(n*2000) runtime, O(2000) space
    DP with counter dicts
    Runtime: 300 ms, faster than 58.85% of Python3 online submissions for Target Sum.
    Memory Usage: 14.4 MB, less than 68.57% of Python3 online submissions for Target Sum.
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ct = collections.Counter({ 0: 1 })
        for n in nums:
            new = collections.Counter()
            for key in ct:
                new[key+n] += ct[key]
                new[key-n] += ct[key]
            ct = new
        return ct[S]

    """
    O(n*2000) runtime and space
    Recursive memoization with LRU cache
    Runtime: 272 ms, faster than 64.45% of Python3 online submissions for Target Sum.
    Memory Usage: 42.2 MB, less than 6.33% of Python3 online submissions for Target Sum.
    """
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     L = len(nums)
    #     @functools.lru_cache(None)
    #     def helper(i=0, cur=0):
    #         if i == L and cur == S:
    #             return 1
    #         if i == L:
    #             return 0
    #         return helper(i+1, cur+nums[i]) + helper(i+1, cur-nums[i])
    #     return helper()

    """
    O(n*2000) runtime and space
    Brute force by reducing to combination sum with LRU caching
    Runtime: 404 ms, faster than 34.49% of Python3 online submissions for Target Sum.
    Memory Usage: 43.8 MB, less than 6.33% of Python3 online submissions for Target Sum.
    """
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    #     ttl = sum(nums)
    #     diff = ttl-S
    #     if diff%2 == 1:
    #         return 0
    #     nums.sort()
    #     tar = diff//2

    #     @functools.lru_cache(None)
    #     def combination_sum(cur=0, s=0):
    #         L = len(nums)
    #         ttl = 0
    #         if cur == tar:
    #             ttl += 1
    #         for i in range(s, L):
    #             v = nums[i]
    #             if cur+v > tar:
    #                 break
    #             ttl += combination_sum(cur+v, i+1)
    #         return ttl

    #     return combination_sum()
