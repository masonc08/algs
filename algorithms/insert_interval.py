"""
Leetcode 57
Runtime: 80 ms, faster than 64.24% of Python3 online submissions for Insert Interval.
Memory Usage: 17.5 MB, less than 18.38% of Python3 online submissions for Insert Interval.
"""


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sol, i, L = [], 0, len(intervals)
        lt, rt = newInterval
        while i < L and intervals[i][1] < lt:
            sol.append(intervals[i])
            i += 1
        while i < L and intervals[i][0] <= rt:
            lt, rt = newInterval
            newInterval = [min(lt, intervals[i][0]), max(rt, intervals[i][1])]
            i += 1
        sol.append(newInterval)
        sol += intervals[i:]
        return sol


Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         if not intervals:
#             return [newInterval]
#         a, b = newInterval
#         i, j = 0, len(intervals)
#         while i < j:
#             m = (i+j)//2
#             v = intervals[m][0]
#             if v == a:
#                 i = m
#                 break
#             elif v < a:
#                 i = m+1
#             else:
#                 j = m
#         if i != 0:
#             sol = intervals[:i-1]
#         i -= 1
#         if i != -1 and intervals[i][1] >= a:
#             # in the middle of an interval or overlapping with left bound
#             a = intervals[i][0]
#             # check if b is also within or on bounds of interval
#             if a <= b <= intervals[i][1]:
#                 b = intervals[i][1]
#         elif i != -1 and a > intervals[i][1]:
#             # between intervals or at the start of an interval
#             sol += intervals[i],
#         while (i := i+1) < len(intervals):
#             l, r = intervals[i]
#             if b < l:
#                 break
#             if l <= b <= r:
#                 b = r
#                 i += 1
#                 break
#         sol += [a, b],
#         sol += intervals[i:]
#         return sol
