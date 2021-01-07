"""
Leetcode 983
Runtime: 56 ms, faster than 21.83% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 14.2 MB, less than 89.77% of Python3 online submissions for Minimum Cost For Tickets.
"""


import bisect


class Solution:
    def mincostTickets(self, days, costs):
        L = len(days)
        dp = [float('inf')]*L
        for i in range(L-1, -1, -1):
            today = days[i]
            for period, cost in zip((1, 7, 30), costs):
                j = bisect.bisect_left(days, today+period, i+1, L)
                dp[i] = min(dp[i], cost+dp[j] if j != L else cost)
        return dp[0]
