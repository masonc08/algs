"""
Leetcode 593
November Leetcoding challenge
Runtime: 32 ms, faster than 73.39% of Python3 online submissions for Valid Square.
Memory Usage: 14 MB, less than 99.78% of Python3 online submissions for Valid Square.
"""


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        sol = set()
        pts = [p1, p2, p3, p4]
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                dist = self._hyp_sqrd(pts[i], pts[j])
                if dist == 0:
                    return False
                sol.add(dist)
        return len(sol) == 2


    def _hyp_sqrd(self, p1, p2):
        return (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
