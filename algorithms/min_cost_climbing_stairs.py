"""
Leetcode 746
Runtime: 84 ms, faster than 5.33% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14.3 MB, less than 63.47% of Python3 online submissions for Min Cost Climbing Stairs.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        pre = cur = 0
        for i in range(2, L+1):
            pre, cur = cur, min(pre+cost[i-2], cur+cost[i-1])
        return cur
