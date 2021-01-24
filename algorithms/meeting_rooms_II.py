"""
Leetcode 253
Runtime: 80 ms, faster than 50.33% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 18 MB, less than 6.21% of Python3 online submissions for Meeting Rooms II.
"""


from itertools import accumulate
from collections import Counter


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mp = Counter()
        for s, e in intervals:
            mp[s] += 1
            mp[e] -= 1
        li = sorted(((k, mp[k]) for k in mp), key=lambda x: x[0])
        li = [b for _, b in li]
        return max(accumulate(li), default=0)
