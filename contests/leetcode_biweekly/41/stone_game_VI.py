"""
Leetcode 1686
Leetcode biweekly contest 41
Runtime: 1308 ms, faster than 50.00% of Python3 online submissions for Stone Game VI.
Memory Usage: 32.4 MB, less than 50.00% of Python3 online submissions for Stone Game VI.
"""


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        a = b = 0
        diff = [(aliceValues[i] + bobValues[i], i)
                for i in range(len(aliceValues))]
        diff.sort(key=lambda x: -x[0])
        for cur, v in enumerate(diff):
            _, i = v
            if cur % 2 == 0:
                a += aliceValues[i]
            else:
                b += bobValues[i]
        if a == b:
            return 0
        if a > b:
            return 1
        return -1
