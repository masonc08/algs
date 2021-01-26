"""
Leetcode 1041
O(n) runtime, O(1) space
Runtime: 20 ms, faster than 99.44% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.4 MB, less than 19.73% of Python3 online submissions for Robot Bounded In Circle.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        x1, y1 = 0, 1
        for c in instructions:
            if c == 'G':
                x, y = x+x1, y+y1
            elif c == 'L':
                x1, y1 = -y1, x1
            elif c == 'R':
                x1, y1 = y1, -x1
            else:
                raise Exception("Incorrect input")
        return (x1, y1) != (0, 1) or (x, y) == (0, 0)
