"""
Leetcode 935
Runtime: 1060 ms, faster than 74.81% of Python3 online submissions for Knight Dialer.
Memory Usage: 14.2 MB, less than 5.49% of Python3 online submissions for Knight Dialer.
"""


class Solution:
    def knightDialer(self, N: int) -> int:
        _mp = (
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4)
        )
        dp = [1]*10
        for _ in range(N-1):
            cur = [0]*10
            for i in range(10):
                for nei in _mp[i]:
                    cur[nei] += dp[i]
                    cur[nei] %= 10**9 + 7
            dp = cur
        return sum(dp)%(10**9+7)


print(Solution().knightDialer(3))