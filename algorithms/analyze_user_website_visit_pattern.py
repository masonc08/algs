"""
Leetcode 1152
Runtime: 48 ms, faster than 85.81% of Python3 online submissions for Analyze User Website Visit Pattern.
Memory Usage: 14.5 MB, less than 94.07% of Python3 online submissions for Analyze User Website Visit Pattern.
"""


import collections
import itertools


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        occ, users = collections.defaultdict(int), collections.defaultdict(list)
        for _, u, w in sorted(zip(timestamp, username, website)):
            users[u].append(w)
        for li in users.values():
            for cmb in set(itertools.combinations(li, 3)):
                occ[cmb] += 1
        return min(occ, key=lambda x: (-occ[x], x))
