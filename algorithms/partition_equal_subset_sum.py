"""
Leetcode 416
November Leetcoding challenges
Runtime: 1348 ms, faster than 50.53% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 89.3 MB, less than 6.12% of Python3 online submissions for Partition Equal Subset Sum.
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2 != 0:
            return False
        target = ttl//2
        cache = [[None]*ttl for _ in range(len(nums))]
        def dfs(i, target):
            if target == 0:
                return True
            if i == len(nums):
                return False
            if cache[i][target] is not None:
                return cache[i][target]
            cache[i][target] = dfs(i+1, target-nums[i]) or dfs(i+1, target)
            return cache[i][target]

        return dfs(0, target)
