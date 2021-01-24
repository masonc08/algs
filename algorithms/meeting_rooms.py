"""
Leetcode 252
O(nlogn) runtime, O(n) space for sorting
Runtime: 68 ms, faster than 93.68% of Python3 online submissions for Meeting Rooms.
Memory Usage: 17.4 MB, less than 57.80% of Python3 online submissions for Meeting Rooms.
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        L = len(intervals)
        for i in range(1, L):
            (a, b), (c, d) = intervals[i-1], intervals[i]
            if a <= c < b:
                return False
        return True