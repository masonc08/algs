"""
Leetcode 735
Runtime: 108 ms, faster than 22.47% of Python3 online submissions for Asteroid Collision.
Memory Usage: 15.5 MB, less than 6.45% of Python3 online submissions for Asteroid Collision.
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        i = 0
        while i < len(asteroids):
            n = asteroids[i]
            if stk and n < 0 and stk[-1] > 0:
                if abs(stk[-1]) < abs(n):
                    stk.pop()
                elif abs(stk[-1]) == abs(n):
                    stk.pop()
                    i += 1
                else:
                    i += 1
            else:
                stk.append(n)
                i += 1
        return stk
