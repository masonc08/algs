"""
Leetcode 62
"""


class Solution:
    """
    Combinatorics solution
    Runtime: 28 ms, faster than 81.84% of Python3 online submissions for Unique Paths.
    Memory Usage: 14.2 MB, less than 47.54% of Python3 online submissions for Unique Paths.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1
        low = min(m-1, n-1)
        high = max(m-1, n-1)
        ttl = low+high
        # sol = (ttl C low) = ttl!/((ttl-low)!low!)
        # a = ttl!/(ttl-low)!
        # b = low!
        # sol = a/b
        a = 1
        for i in range(ttl-low+1, ttl+1):
            a *= i
        b = 1
        for i in range(1, low+1):
            b *= i
        return a//b

    """
    DP solution
    Runtime: 32 ms, faster than 55.05% of Python3 online submissions for Unique Paths.
    Memory Usage: 14.2 MB, less than 46.97% of Python3 online submissions for Unique Paths.
    """
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [1]*n
    #     for _ in range(1, m):
    #         new = [0]*n
    #         for j in range(n):
    #             if j != 0:
    #                 new[j] = new[j-1]+dp[j]
    #             else:
    #                 new[j] = dp[j]
    #         dp = new
    #     return dp[-1]
