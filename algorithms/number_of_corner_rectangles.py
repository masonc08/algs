"""
Leetcode 750
January Leetcoding challenge
O(m^2n) runtime, O(m*n) space
Runtime: 624 ms, faster than 99.20% of Python3 online submissions for Number Of Corner Rectangles.
Memory Usage: 15.6 MB, less than 70.40% of Python3 online submissions for Number Of Corner Rectangles.
"""


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        dp, sol = [], 0
        for row in grid:
            cur = set(i for i, v in enumerate(row) if v)
            for prow in dp:
                intersect = len(cur&prow)
                sol += intersect*(intersect-1)//2
            dp.append(cur)
        return sol
