"""
Leetcode 1673
Leetcode weekly contest 217
"""


import heapq


class Solution:
    """
    O(n) runtime and space using stack
    Runtime: 1240 ms, faster than 50.00% of Python3 online submissions for Find the Most Competitive Subsequence.
    Memory Usage: 27.6 MB, less than 50.00% of Python3 online submissions for Find the Most Competitive Subsequence.
    """
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        sol = []
        for i, v in enumerate(nums):
            while sol and sol[-1] > v and len(sol)+len(nums)-i-1 >= k:
                sol.pop()
            if len(sol) < k:
                sol.append(v)
        return sol


    """
    O(nlogn) runtime, O(n) space using heap
    """
    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     heap = []
    #     for i in range(len(nums)-k+1):
    #         heapq.heappush(heap, (nums[i], i))
    #     sol = []
    #     i = len(nums)-k+1
    #     last = -1
    #     while k:
    #         lowest, idx = heap[0]
    #         while idx < last:
    #             heapq.heappop(heap)
    #             lowest, idx = heap[0]
    #         heapq.heappop(heap)
    #         sol.append(lowest)
    #         last = idx
    #         k -= 1
    #         if i != len(nums):
    #             heapq.heappush(heap, (nums[i], i))
    #         i += 1
    #     return sol
