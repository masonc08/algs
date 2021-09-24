import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        buckets = [[] for _ in nums] + [[]]
        for char, v in ct.items():
            buckets[v].append(char)
        sol = []
        for li in reversed(buckets):
            sol += li[:k-len(sol)]
            if len(sol) == k:
                return sol
        raise Exception()


# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     occurrences = {}
#     for num in nums:
#         occurrences[num] = occurrences.get(num, 0) + 1
#     sol = [None]*k
#     for i in range(k):
#         largest = (None, 0)
#         for key, value in occurrences.values():
#             if value > largest[1]:
#                 largest = (key, value)
#         sol[i] = largest[0]
#         del occurrences[largest[0]]
#     return sol
