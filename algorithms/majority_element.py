"""
Leetcode 169
"""


import collections


class Solution:
    """
    O(n) runtime, O(1) space, Boyer-Moore voting algorithm
    Runtime: 168 ms, faster than 38.61% of Python3 online submissions for Majority Element.
    Memory Usage: 15.5 MB, less than 18.99% of Python3 online submissions for Majority Element.
    """
    def majorityElement(self, nums: List[int]) -> int:
        cand = count = 0
        for num in nums:
            if count == 0:
                cand = num
            if cand == num:
                count += 1
            else:
                count -= 1
        return cand


    """
    O(n) runtime and space, first-past-the-post system
    Runtime: 184 ms, faster than 10.21% of Python3 online submissions for Majority Element.
    Memory Usage: 15.4 MB, less than 64.86% of Python3 online submissions for Majority Element.
    """
    # def majorityElement(self, nums: List[int]) -> int:
    #     post = len(nums)//2
    #     ct = collections.Counter()
    #     for num in nums:
    #         ct[num] += 1
    #         if ct[num] > post:
    #             return num
    #     raise Exception()
