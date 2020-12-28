"""
Leetcode 754
December Leetcoding challenge
Runtime: 92 ms, faster than 52.06% of Python3 online submissions for Reach a Number.
Memory Usage: 14.1 MB, less than 56.16% of Python3 online submissions for Reach a Number.
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        cur = jumps = 0
        target = abs(target)
        while cur < target:
            jumps += 1
            cur += jumps
        return jumps if (target-cur)%2 == 0 else jumps+1+jumps%2
