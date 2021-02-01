"""
Leetcode 1654
Leetcode biweekly contest 39
Runtime: 84 ms, faster than 100.00% of Python3 online submissions for Minimum Jumps to Reach Home.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Minimum Jumps to Reach Home.
"""


import math
import collections
from typing import List


# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         forbidden_max = max(forbidden)
#         max_dist = max(x, forbidden_max)+a+b
#         jumps = [0] + [math.inf]*max_dist
#         for i in forbidden:
#             jumps[i] = -1
#         q = collections.deque([0])
#         while q:
#             loc = q.popleft()
#             if loc+a <= max_dist and jumps[loc+a] > jumps[loc]+1:
#                 jumps[loc+a] = jumps[loc]+1
#                 q.append(loc+a)
#             if loc-b > 0 and jumps[loc-b] > jumps[loc]+1:
#                 jumps[loc-b] = jumps[loc]+1
#                 if loc-b+a <= max_dist and jumps[loc-b+a] > jumps[loc]+2:
#                     jumps[loc-b+a] = jumps[loc]+2
#                     q.append(loc-b+a)
#         return jumps[x] if jumps[x] < math.inf else -1

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
      	if x == 0:
          	return 0
		fbden_set, visited = set(forbidden), set([0])
        q = collections.deque(((0, 0),))
        while q:
        	node, wave = q.popleft()
            if node+a == x or node-b == x:
            	return wave+1
            if node+a <= x+a+1 and node+a not in forbidden and node+a not in visited:
                visited.add(node+a)
                q.append((node+a, wave+1))
            if node-b >= 0 and node-b+a >= 0 and node-b not in forbidden and \
            node-b+a not in forbidden and node-b+a not in visited:
                if node-b+a == x:
                    return wave+2
                visited.add(node-b+a)
                q.append((node-b+a, wave+2))
        return -1