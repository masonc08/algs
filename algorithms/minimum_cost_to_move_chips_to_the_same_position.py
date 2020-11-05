"""
Leetcode 1217
November Leetcoding Challenge
Runtime: 28 ms, faster than 86.97% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
Memory Usage: 14.2 MB, less than 99.86% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
"""

class Solution:
    def minCostToMoveChips(self, positions: List[int]) -> int:
        odds, evens = 0, 0
        for position in positions:
            if position%2 == 1:
                odds += 1
            else:
                evens += 1
        return min(odds, evens)
