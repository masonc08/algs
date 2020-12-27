"""
Leetcode 554
Runtime: 196 ms, faster than 17.53% of Python3 online submissions for Brick Wall.
Memory Usage: 19.1 MB, less than 38.26% of Python3 online submissions for Brick Wall.
"""

import collections
import itertools


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ct = collections.Counter()
        for row in wall:
            ct.update(itertools.accumulate(row[:-1]))
        return len(wall)-ct.most_common(1)[0][1] if ct else len(wall)

# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         if not wall:
#             return 0
#         m = len(wall)
#         ends = set()
#         rows_ends = []
#         # O(m*max(n))
#         for row in wall:
#             cur = set()
#             for i in range(len(row)-1):
#                 if i != 0:
#                     row[i] += row[i-1]
#                 cur.add(row[i])
#                 ends.add(row[i])
#         rows_ends += cur,
#         sol = 0    # number of brick edges traversed
#         # O(items in matrix)
#         # O(m*max(n))
#         for x in ends:
#             ttl = 0
#             for row in rows_ends:
#                 if x in row:
#                 ttl += 1
#             sol = max(sol, ttl)
#         return m-sol