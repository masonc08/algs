"""
Leetcode 790
O(N9) runtime, O(3*4) space
DP
Runtime: 52 ms, faster than 20.48% of Python3 online submissions for Domino and Tromino Tiling.
Memory Usage: 14.1 MB, less than 82.53% of Python3 online submissions for Domino and Tromino Tiling.
"""


class Solution:
    STATES = (
        ((1, 0), (0, 3), (1, 1), (1, 2)),
        ((2, 0), (1, 2)),
        ((2, 0), (1, 1)),
        ((2, 0),)
    )
    MOD = 1000000007
    def numTilings(self, N: int) -> int:
        L = len(self.STATES)
        dp = [[0]*L for _ in range(3)]
        dp[0][0] = 1
        for _ in range(N):
            for i, state in enumerate(self.STATES):
                for i1, j1 in state:
                    dp[i1][j1] = (dp[i1][j1]+dp[0][i])%self.MOD
            dp[0], dp[1], dp[2] = dp[1], dp[2], [0]*L
        return dp[0][0]
