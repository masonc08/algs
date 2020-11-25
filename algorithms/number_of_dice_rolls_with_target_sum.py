"""
Leetcode 1155
Runtime: 692 ms, faster than 31.56% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 20.3 MB, less than 24.97% of Python3 online submissions for Number of Dice Rolls With Target Sum.
"""


class Solution:
    def numRollsToTarget(self, a: int, b: int, c: int) -> int:
        mp = {}
        def helper(d, f, target):
            if d == 0 and target == 0:
                return 1
            if d <= 0 or target <= 0:
                return 0
            if (d, target) in mp:
                return mp[(d, target)]
            sol = 0
            for i in range(1, f+1):
                if i > target:
                    break
                sol += helper(d-1, f, target-i)
                sol %= (10**9+7)
            mp[(d, target)] = sol
            return sol

        return helper(a, b, c)
