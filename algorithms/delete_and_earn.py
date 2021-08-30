"""
Leetcode 740
O(n+mlogm) runtime, O(m) space. n=input size, m=max(A)
Runtime: 73 ms, faster than 23.79% of Python3 online submissions for Delete and Earn.
Memory Usage: 14.4 MB, less than 82.52% of Python3 online submissions for Delete and Earn.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ct = collections.Counter(nums)
        last_taken = last_not_taken = 0
        for num in sorted(ct):
            last_taken, last_not_taken = num*ct[num] + last_not_taken, max(last_taken, last_not_taken)
            if num+1 not in ct:
                last_taken = last_not_taken = max(last_taken, last_not_taken)
        return max(last_taken, last_not_taken)
