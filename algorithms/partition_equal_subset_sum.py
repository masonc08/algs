"""
Leetcode 416
November Leetcoding challenges
"""


from typing import List


class Solution:
    """
    O(NS) runtime, O(S) space, N=n, S=sum(N)//2
    DP solution, 01 knapsack style
    Runtime: 1152 ms, faster than 56.03% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 14.4 MB, less than 66.43% of Python3 online submissions for Partition Equal Subset Sum.
    """
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl%2 != 0:
            return False
        target = ttl//2
        dp = [False]*(ttl+1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[target]


    """
    O(NS) runtime, O(NS) space, N=n, S=sum(N)//2
    DFS Solution with memoization
    Runtime: 1348 ms, faster than 50.53% of Python3 online submissions for Partition Equal Subset Sum.
    Memory Usage: 89.3 MB, less than 6.12% of Python3 online submissions for Partition Equal Subset Sum.
    """
    # def canPartition(self, nums: List[int]) -> bool:
    #     ttl = sum(nums)
    #     if ttl%2 != 0:
    #         return False
    #     target = ttl//2
    #     cache = [[None]*ttl for _ in range(len(nums))]
    #     def dfs(i, target):
    #         if target == 0:
    #             return True
    #         if i == len(nums):
    #             return False
    #         if cache[i][target] is not None:
    #             return cache[i][target]
    #         cache[i][target] = dfs(i+1, target-nums[i]) or dfs(i+1, target)
    #         return cache[i][target]

    #     return dfs(0, target)
