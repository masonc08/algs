"""
Leetcode 78
Runtime: 28 ms, faster than 93.29% of Python3 online submissions for Subsets.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Subsets.
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        sol, cur = [[]], []
        def subsets(i=0):
            cur.append(nums[i])
            sol.append(cur.copy())
            for j in range(i+1, len(nums)):
                subsets(j)
            cur.pop()
        for i in range(len(nums)):
            subsets(i)
        return sol
