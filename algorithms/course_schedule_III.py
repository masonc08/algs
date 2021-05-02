"""
Leetcode 630
May Leetcoding challenge
O(nlogn) runtime, O(n) space
Runtime: 680 ms, faster than 87.74% of Python3 online submissions for Course Schedule III.
Memory Usage: 19.3 MB, less than 90.65% of Python3 online submissions for Course Schedule III.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq, ttl = [], 0
        for dur, dead in sorted(courses, key=lambda x: x[1]):
            if dur + ttl <= dead:
                ttl += dur
                heapq.heappush(pq, -dur)
            elif pq and -pq[0] > dur:
                ttl = ttl - (-heapq.heappop(pq)) + dur
                heapq.heappush(pq, -dur)
        return len(pq)

