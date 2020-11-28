"""
Leetcode 239
November Leetcoding challenge
"""


import heapq
import collections
from typing import List


class Solution:
    """
    O(n) runtime, O(n) space, using linked list
    Runtime: 1408 ms, faster than 51.58% of Python3 online submissions for Sliding Window Maximum.
    Memory Usage: 30.3 MB, less than 23.78% of Python3 online submissions for Sliding Window Maximum.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ll = collections.deque()
        sol = [0]*(len(nums)-k+1)
        for i, num in enumerate(nums):
            while ll and nums[ll[-1]] < num:
                ll.pop()
            ll.append(i)
            if ll[0] < i-k+1:
                ll.popleft()
            if i-k+1 >= 0:
                sol[i-k+1] = nums[ll[0]]
        return sol


    """
    O(n) runtime and space, using heap
    Runtime: 1572 ms, faster than 17.91% of Python3 online submissions for Sliding Window Maximum.
    Memory Usage: 41 MB, less than 5.25% of Python3 online submissions for Sliding Window Maximum.
    """
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     heap = []
    #     tracker = [None]*len(nums)
    #     for i in range(k):
    #         tmp = [-nums[i], True]
    #         tracker[i] = tmp
    #         heapq.heappush(heap, tmp)
    #     sol = [0]*(len(nums)-k+1)
    #     sol[0], _ = heap[0]
    #     sol[0] = -sol[0]
    #     for i in range(1, len(sol)):
    #         x = [-nums[i+k-1], True]
    #         tracker[i+k-1] = x
    #         heapq.heappush(heap, x)
    #         tracker[i-1][1] = False
    #         x, valid = heap[0]
    #         while not valid:
    #             heapq.heappop(heap)
    #             x, valid = heap[0]
    #         sol[i] = -x
    #     return sol
