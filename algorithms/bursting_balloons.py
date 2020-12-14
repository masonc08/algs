"""
Leetcode 312
December Leetcoding challenge
Runtime: 908 ms, faster than 8.07% of Python3 online submissions for Burst Balloons.
Memory Usage: 15 MB, less than 40.99% of Python3 online submissions for Burst Balloons.
"""


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = [[0]*len(nums) for _ in nums]
        for i in range(len(nums)): # size of subarray
            for j in range(len(nums)-i): # subarray starting at j
                for k in range(j, j+i+1): # number in subarray
                    cur = 0
                    if k-1 >= 0:
                        cur += dp[j][k-1]
                    if k+1 < len(nums):
                        cur += dp[k+1][j+i]
                    a = nums[j-1] if j-1 >= 0 else 1
                    b = nums[j+i+1] if j+i+1 < len(nums) else 1
                    cur += (a*nums[k]*b)
                    dp[j][j+i] = max(dp[j][j+i], cur)
        return dp[0][-1]
