"""
Leetcode 218
Runtime: 188 ms, faster than 23.02% of Python3 online submissions for The Skyline Problem.
Memory Usage: 20.5 MB, less than 14.40% of Python3 online submissions for The Skyline Problem.
"""


from sortedcontainers import SortedDict
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pts = [None]*(len(buildings)*2)
        for i, v in enumerate(buildings):
            l, r, h = v
            pts[i] = (l, h, 's')
            pts[len(pts)-i-1] = (r, h, 'e')
        pts.sort(key=lambda x: (x[0], -x[1] if x[2] == 's' else x[1]))
        sol = []
        pq = SortedDict({ 0: 1 })
        for x, y, t in pts:
            prev, _ = pq.peekitem(index=-1)
            if t == 's':
                pq[y] = pq.get(y, 0) + 1
                cur, _ = pq.peekitem(index=-1)
                if cur > prev:
                    sol.append([x, y])
            else:
                pq[y] = pq[y]-1
                if pq[y] == 0:
                    del pq[y]
                cur, _ = pq.peekitem(index=-1)
                if cur < prev:
                    sol.append([x, cur])
        return sol
