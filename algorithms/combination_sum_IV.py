"""
Leetcode 377
Runtime: 36 ms, faster than 95.16% of Python3 online submissions for Combination Sum IV.
Memory Usage: 14.6 MB, less than 33.98% of Python3 online submissions for Combination Sum IV.
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
                if num > i:
                    break
        return dp[-1]
