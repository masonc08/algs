"""
Leetcode 781
O(n) runtime and space
Runtime: 36 ms, faster than 94.35% of Python3 online submissions for Rabbits in Forest.
Memory Usage: 14.5 MB, less than 32.86% of Python3 online submissions for Rabbits in Forest.
"""


import collections
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ct = collections.Counter(answers)
        return sum(math.ceil(ct[k]/(k+1))*(k+1) for k in ct)


# class Solution:
#     def numRabbits(self, A: List[int]) -> int:
#         mp = {}
#         for a in A:
#             if a == 0:
#                 continue
#             if a in mp:
#                 mp[a] -= 1
#                 if mp[a] == 0:
#                     del mp[a]
#             else:
#                 mp[a] = a
#         return len(A)+sum(mp.values())
        