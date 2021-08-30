"""
Leetcode 915
July Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


"""
O(n) runtime and space, 3-pass
Runtime: 204 ms, faster than 56.46% of Python3 online submissions for Partition Array into Disjoint Intervals.
Memory Usage: 18.5 MB, less than 31.18% of Python3 online submissions for Partition Array into Disjoint Intervals.
"""
# class Solution:
#     def partitionDisjoint(self, nums: List[int]) -> int:
#         mins = []
#         for i, num in enumerate(nums):
#             while mins and nums[mins[-1]] >= num:
#                 mins.pop()
#             mins.append(i)
#         cur, i = -math.inf, 0
#         for j, num in enumerate(nums):
#             cur = max(cur, num)
#             if j >= mins[i]:
#                 i += 1
#             if cur <= nums[mins[i]]:
#                 return j+1
#         raise Exception("No solution")


"""
O(n) runtime, O(1) space, 1-pass
Runtime: 180 ms, faster than 87.36% of Python3 online submissions for Partition Array into Disjoint Intervals.
Memory Usage: 18.1 MB, less than 99.72% of Python3 online submissions for Partition Array into Disjoint Intervals.
"""
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        cur, sol, prev = nums[0], 0, nums[0]
        for i, num in enumerate(nums):
            cur = max(cur, num)
            if num < prev:
                prev = cur
                sol = i
        return sol+1
