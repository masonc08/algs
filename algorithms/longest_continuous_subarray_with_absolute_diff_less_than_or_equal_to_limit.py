"""
Leetcode 1438
"""


import sortedcontainers
import collections


class Solution:
    """
    O(n) runtime and space using linkedlist to track mins/maxes of sliding window
    Runtime: 812 ms, faster than 35.22% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Memory Usage: 24.4 MB, less than 18.93% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sol = 1
        i = j = 0
        mins, maxs = collections.deque([nums[i]]), collections.deque([nums[i]])
        lowest = highest = mins[0]
        while i < len(nums) and j < len(nums):
            if highest-lowest > limit:
                i += 1
                if i != len(nums):
                    if nums[i-1] == mins[0]:
                        mins.popleft()
                    if nums[i-1] == maxs[0]:
                        maxs.popleft()
                    lowest, highest = mins[0], maxs[0]
            else:
                sol = max(sol, j-i+1)
                j += 1
                if j != len(nums):
                    while maxs and nums[j] > maxs[-1]:
                        maxs.pop()
                    while mins and nums[j] < mins[-1]:
                        mins.pop()
                    maxs.append(nums[j])
                    mins.append(nums[j])
                    lowest, highest = mins[0], maxs[0]
        return sol


    """
    O(nlogn) runtime, O(n) space using sortedlist
    Runtime: 1680 ms, faster than 9.04% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Memory Usage: 24 MB, less than 63.85% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    """
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     sol = 1
    #     i = j = 0
    #     pq = sortedcontainers.SortedList([nums[i]])
    #     lowest = highest = pq[0]
    #     while i < len(nums) and j < len(nums):
    #         if highest-lowest > limit:
    #             i += 1
    #             if i != len(nums):
    #                 pq.remove(nums[i-1])
    #                 lowest, highest = pq[0], pq[-1]
    #         else:
    #             sol = max(sol, j-i+1)
    #             j += 1
    #             if j != len(nums):
    #                 pq.add(nums[j])
    #                 lowest, highest = pq[0], pq[-1]
    #     return sol
 