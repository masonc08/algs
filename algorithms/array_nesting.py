"""
Leetcode 565
September Leetcoding challenge
O(n) runtime, O(1) space
Runtime: 120 ms, faster than 60.53% of Python3 online submissions for Array Nesting.
Memory Usage: 16 MB, less than 94.52% of Python3 online submissions for Array Nesting.
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
	def arrayNesting(self, nums: List[int]) -> int:
		L, sol = len(nums), -math.inf
		for i in range(L):
			cur = 0
			while nums[i] != 0x7fffffff:
				nums[i], i = 0x7fffffff, nums[i]
				cur += 1
			sol = max(sol, cur)
		return sol
