"""
Leetcode 134
Runtime: 48 ms, faster than 88.22% of Python3 online submissions for Gas Station.
Memory Usage: 15.2 MB, less than 37.47% of Python3 online submissions for Gas Station.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = need = depart = 0
        for i, (a, b) in enumerate(zip(gas, cost)):
            if a-b > 0 and cur < 0:
                need += -cur
                cur = 0
                depart = i
            cur += a-b
        return depart if cur >= need else -1
