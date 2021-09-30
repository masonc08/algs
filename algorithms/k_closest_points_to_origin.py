"""
Leetcode 973

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    # O(n) average time, O(k) space
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(x, y):
            return x*x+y*y
        i, j = 0, len(points)-1
        while j-i+1 > 1:
            pivot = random.randrange(i, j+1)
            points[pivot], points[j] = points[j], points[pivot]
            a, b = i, j-1
            while a < b:
                if dist(*points[a]) > dist(*points[j]):
                    points[a], points[b] = points[b], points[a]
                    b -= 1
                else:
                    a += 1
            a = a+1 if dist(*points[a]) <= dist(*points[j]) else a
            points[a], points[j] = points[j], points[a]
            j = a-1 if a > K else j
            i = a+1 if a < K else i
            if a == K:
                break
        return points[:K]
        
    # O(nlogk) runtime, O(k) space
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     def dist(point):
    #         x, y = point
    #         return x*x+y*y
    #     hp = []
    #     for point in points:
    #         heapq.heappush(hp, (-dist(point), point))
    #         if len(hp) == K+1:
    #             heapq.heappop(hp)
    #     return [v for _, v in hp]
