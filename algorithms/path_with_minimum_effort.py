"""
Leetcode 1631
January Leetcoding challenge
"""


import heapq


"""
Binary search with DFS pathfinding
O(MNlog(K)) runtime, O(MN) space, where K is max(heights)
Runtime: 2168 ms, faster than 21.16% of Python3 online submissions for Path With Minimum Effort.
Memory Usage: 20.9 MB, less than 10.12% of Python3 online submissions for Path With Minimum Effort.
"""
class Solution:
    _DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        def can_reach(lim, i=0, j=0):
            seen[i][j] = True
            if (i, j) == (m-1, n-1):
                return True
            for i1, j1 in self._DIRS:
                if m > i+i1 >= 0 <= j+j1 < n and not seen[i+i1][j+j1] and \
                    abs(heights[i][j]-heights[i+i1][j+j1]) <= lim and can_reach(lim, i+i1, j+j1):
                    return True
            return False
        s, e = 0, max(map(max, heights))
        while s < e:
            mid = s+e>>1
            seen = [[False]*n for _ in range(m)]
            if can_reach(mid):
                e = mid
            else:
                s = mid+1
        return s

"""
Dijkstra's Algorithm
O(MNlog(MN)) runtime, O(MN) space
Runtime: 748 ms, faster than 74.81% of Python3 online submissions for Path With Minimum Effort.
Memory Usage: 15.3 MB, less than 91.17% of Python3 online submissions for Path With Minimum Effort.
"""
# class Solution:
#     _DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1))

#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         m, n = len(heights), len(heights[0])
#         dp = [[float('inf')]*n for _ in range(m)]
#         dp[0][0] = 0
#         hp = [(0, 0, 0)]
#         while hp:
#             d, i, j = heapq.heappop(hp)
#             if (i, j) == (m-1, n-1):
#                 return d
#             if d > dp[i][j]:
#                 continue
#             for i1, j1 in self._DIRS:
#                 if 0 <= i+i1 < m and 0 <= j+j1 < n:
#                     cand = max(d, abs(heights[i][j]-heights[i+i1][j+j1]))
#                     if cand < dp[i+i1][j+j1]:
#                         dp[i+i1][j+j1] = cand
#                         heapq.heappush(hp, (cand, i+i1, j+j1))
#         raise Exception("Endpoint was never reached")
