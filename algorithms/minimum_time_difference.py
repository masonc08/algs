"""
Leetcode 539
"""


"""
O(n) runtime, O(1) space by bucket sorting
Runtime: 68 ms, faster than 82.75% of Python3 online submissions for Minimum Time Difference.
Memory Usage: 17 MB, less than 74.18% of Python3 online submissions for Minimum Time Difference.
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) >= 60*24:
            return 0
        bkt = [False]*(60*24)
        for t in timePoints:
            h, m = t.split(':')
            h, m = int(h), int(m)
            x = h*60+m
            if bkt[x]:
                return 0
            bkt[x] = True
        sol = float('inf')
        first, prev = None, None
        for i, v in enumerate(bkt):
            if v:
                if prev is None:
                    first = i
                else:
                    sol = min(sol, v-prev)
                prev = i
        return min(sol, 60*24+first-prev)


"""
O(nlogn) runtime, O(n) space due to Timsort
Runtime: 104 ms, faster than 10.58% of Python3 online submissions for Minimum Time Difference.
Memory Usage: 17.2 MB, less than 11.84% of Python3 online submissions for Minimum Time Difference.
"""
# class Solution: 
#     def findMinDifference(self, timePoints: List[str]) -> int:
#         L = len(timePoints)
#         timePoints.sort(key=lambda x: (int(x[:2]), int(x[3:])))
#         sol = 60*24-self.diff(timePoints[0], timePoints[-1])
#         for i in range(L-1):
#             diff = self.diff(timePoints[i], timePoints[i+1])
#             sol = min((diff, 60*24-diff, sol))
#         return sol

#     def diff(self, a, b):
#         (ha, ma), (hb, mb) = a.split(':'), b.split(':')
#         ha, ma, hb, mb = int(ha), int(ma), int(hb), int(mb)
#         if mb < ma:
#             mb += 60
#             hb -= 1
#         return mb-ma+(hb-ha)*60
