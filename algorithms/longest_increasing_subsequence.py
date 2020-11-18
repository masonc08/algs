"""
Leetcode 300
"""


from typing import List


class Solution:
    """
    Dynamic Program using binary search to query cache
    O(nlogn) runtime, O(n) space
    Runtime: 76 ms, faster than 73.14% of Python3 online submissions for Longest Increasing Subsequence.
    Memory Usage: 14.3 MB, less than 71.61% of Python3 online submissions for Longest Increasing Subsequence.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp_size = 0
        for num in nums:
            i, j = 0, dp_size
            while i != j:
                mid = (i+j)//2
                if dp[mid] < num:
                    i = mid+1
                else:
                    j = mid
            dp[i] = num
            if i == dp_size:
                dp_size += 1
        return dp_size

    """
    Dynamic Program
    O(n^2) runtime, O(n) space
    Runtime: 3324 ms, faster than 5.01% of Python3 online submissions for Longest Increasing Subsequence.
    Memory Usage: 14.4 MB, less than 35.01% of Python3 online submissions for Longest Increasing Subsequence.
    """
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [0]*len(nums)
    #     sol = 0
    #     for i in range(len(nums)):
    #         v0 = nums[i]
    #         max_subseq = 0
    #         for j in range(i):
    #             v1 = nums[j]
    #             if v1 < v0:
    #                 max_subseq = max(max_subseq, dp[j])
    #         dp[i] = max_subseq+1
    #         sol = max(dp[i], sol)
    #     return sol

Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
