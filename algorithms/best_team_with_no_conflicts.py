"""
Leetcode 1626
Runtime: 1780 ms, faster than 73.37% of Python3 online submissions for Best Team With No Conflicts.
Memory Usage: 14.7 MB, less than 44.67% of Python3 online submissions for Best Team With No Conflicts.
"""


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        L = len(ages)
        dp = [0]*L
        data = list(zip(ages, scores))
        data.sort()
        sol = 0
        for i, (_, score) in enumerate(data):
            dp[i] = score
            for j in range(i-1, -1, -1):
                if score >= data[j][1]:
                    dp[i] = max(dp[j]+score, dp[i])
            sol = max(sol, dp[i])
        return sol
