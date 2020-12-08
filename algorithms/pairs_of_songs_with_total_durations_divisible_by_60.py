"""
Leetcode 1010
Runtime: 236 ms, faster than 34.69% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 17.9 MB, less than 67.25% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
"""


import collections


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = collections.defaultdict(int)
        sol = 0
        for n in time:
            sol += mp[(60-(n%60))%60]
            mp[n%60] += 1
        return sol
