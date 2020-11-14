"""
Leetcode 1653
Leetcode biweekly contest 39
Runtime: 388 ms, faster than 100.00% of Python3 online submissions for Minimum Deletions to Make String Balanced.
Memory Usage: 14.9 MB, less than 25.00% of Python3 online submissions for Minimum Deletions to Make String Balanced.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp, b_count = 0, 0
        for c in s:
            if c == 'a':
                dp = min(dp+1, b_count)
            else:
                b_count += 1
        return dp
