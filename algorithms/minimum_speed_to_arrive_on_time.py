"""
Leetcode 1870
Runtime: 3640 ms, faster than 58.55% of Python3 online submissions for Minimum Speed to Arrive on Time.
Memory Usage: 28.2 MB, less than 91.19% of Python3 online submissions for Minimum Speed to Arrive on Time.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
	def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
		L = len(dist)
		A, B = dist[:-1], dist[-1]
		bound = math.ceil(max(dist)/(hour/L))
		lo, hi = 1, bound
		mid = (lo+hi)//2
		while lo < hi:
			mid = (lo+hi)//2
			total_time = self.get_time(mid, A, B)
			if total_time <= hour:
				# if arrive early for work, or on time, we will try going slower next time
				hi = mid
			else:
				# if arrive late for work, we will try going faster next time
				# but we wont ever go at the same speed again because we know we'll be late
				lo = mid+1
		return lo if lo <= bound and self.get_time(lo, A, B) <= hour else -1

	def get_time(self, speed, A, B):
		return sum(math.ceil(dist/speed) for dist in A) + B/speed
