"""
Leetcode 220
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math
import sortedcontainers

"""
BIT, O(nlogk) runtime, O(k) space
Runtime: 576 ms, faster than 9.23% of Python3 online submissions for Contains Duplicate III.
Memory Usage: 17.2 MB, less than 89.59% of Python3 online submissions for Contains Duplicate III.
"""
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         tree = sortedcontainers.SortedList()
#         for i, v in enumerate(nums):
#             tree.add(v)
#             if i > k:
#                 tree.remove(nums[i-k-1])
#             j = tree.index(v)
#             L = len(tree)
#             if j != 0 and abs(v-tree[j-1]) <= t or \
#                 j != L-1 and abs(v-tree[j+1]) <= t:
#                 return True
#         return False

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets, num_buckets = {}, t+1
        for i, num in enumerate(nums):
            if i > k:
                del buckets[nums[i-k-1]//num_buckets]
            bucket = num//num_buckets
            if bucket in buckets \
                or bucket-1 in buckets and abs(buckets[bucket-1]-num) <= t \
                    or bucket+1 in buckets and abs(buckets[bucket+1]-num) <= t:
                return True
            buckets[bucket] = num
        return False