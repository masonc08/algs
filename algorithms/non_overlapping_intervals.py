"""
Leetcode 435
Runtime: 72 ms, faster than 55.38% of Python3 online submissions for Non-overlapping Intervals.
Memory Usage: 17.5 MB, less than 50.07% of Python3 online submissions for Non-overlapping Intervals.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        sol = 1
        if not intervals:
            return 0
        p = intervals[0][1]
        L = len(intervals)
        for i in range(1, L):
            s, e = intervals[i]
            if s >= p:
                sol += 1
                p = e
        return L-sol
