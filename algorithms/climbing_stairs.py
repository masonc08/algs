"""
Leetcode 70, Daily Coding Problem #12
"""


class Solution:
    """
    O(NS) runtime, O(N) space, N=n, S=len(STEPS)
    Generalized DP solution for x amount of steps
    Runtime: 24 ms, faster than 94.17% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 14.3 MB, less than 10.21% of Python3 online submissions for Climbing Stairs.
    """
    STEPS = {1, 2}
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        for step in self.STEPS:
            if step <= n:
                dp[step] = 1
        for i in range(1, n+1):
            for step in self.STEPS:
                dp[i] += dp[i-step] if i-step >= 0 else 0
        return dp[n]



    # def climbStairs(self, n: int) -> int:
    #     if n == 1 or n == 0:
    #         return 1
    #     last_two = [0]*2
    #     last_two[0], last_two[1] = 1, 1
    #     for i in range(2, n):
    #         last_two[0], last_two[1] = last_two[1], last_two[0]
    #         temp = sum(last_two)
    #         last_two[1] = temp
    #     return sum(last_two)
