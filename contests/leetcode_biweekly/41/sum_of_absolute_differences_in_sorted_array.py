"""
Leetcode 1685
Leetcode biweekly contest 41
Runtime: 1032 ms, faster than 25.00% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
Memory Usage: 29.2 MB, less than 50.00% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        cur = 0
        for num in nums:
            cur += abs(nums[0] - num)
        sol = [0] * len(nums)
        sol[0] = cur
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            sol[i] = sol[i - 1]
            sol[i] -= ((len(nums) - i - 1) * diff)
            sol[i] += ((i - 1) * diff)
        return sol
