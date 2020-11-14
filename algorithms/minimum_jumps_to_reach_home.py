"""
Leetcode 1654
Leetcode biweekly contest 39
Runtime: 84 ms, faster than 100.00% of Python3 online submissions for Minimum Jumps to Reach Home.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Minimum Jumps to Reach Home.
"""


import math
import collections
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_max = max(forbidden)
        max_dist = max(x, forbidden_max)+a+b
        jumps = [0] + [math.inf]*max_dist
        for i in forbidden:
            jumps[i] = -1
        q = collections.deque([0])
        while q:
            loc = q.popleft()
            if loc+a <= max_dist and jumps[loc+a] > jumps[loc]+1:
                jumps[loc+a] = jumps[loc]+1
                q.append(loc+a)
            if loc-b > 0 and jumps[loc-b] > jumps[loc]+1:
                jumps[loc-b] = jumps[loc]+1
                if loc-b+a <= max_dist and jumps[loc-b+a] > jumps[loc]+2:
                    jumps[loc-b+a] = jumps[loc]+2
                    q.append(loc-b+a)
        return jumps[x] if jumps[x] < math.inf else -1
