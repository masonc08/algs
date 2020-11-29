"""
Leetcode 45
"""


class Solution:
    """
    O(n) runtime, O(1) space
    Runtime: 144 ms, faster than 13.96% of Python3 online submissions for Jump Game II.
    Memory Usage: 16 MB, less than 94.08% of Python3 online submissions for Jump Game II.
    """
    def jump(self, nums: List[int]) -> int:
        i = jumps = prev = 0
        while i < len(nums)-1:
            jumps += 1
            lim = prev+nums[prev]
            if lim >= len(nums)-1:
                return jumps
            for j in range(i+1, lim+1):
                if j+nums[j] >= len(nums)-1:
                    return jumps+1
                if j+nums[j] > prev+nums[prev]:
                    prev = j
            i = j-1
        return jumps


    """
    O(n^2) runtime, O(n) space dp solution
    """
    # def jump(self, nums: List[int]) -> int:
    #     dp = [0]*len(nums)
    #     for i in range(len(nums)-2, -1, -1):
    #         v = nums[i]
    #         lowest = len(nums)
    #         for j in range(1, v+1):
    #             if i+j >= len(nums):
    #                 break
    #             lowest = min(dp[i+j], lowest)
    #         dp[i] = 1+lowest
    #     return dp[0]
