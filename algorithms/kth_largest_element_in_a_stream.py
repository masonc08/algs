"""
Leetcode 703
Runtime: 100 ms, faster than 50.41% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.3 MB, less than 21.19% of Python3 online submissions for Kth Largest Element in a Stream.
"""


import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            heapq.heappushpop(self.heap, nums[i])


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif len(self.heap) == self.k and val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)