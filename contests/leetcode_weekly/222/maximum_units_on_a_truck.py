"""
Leetcode 1710
Leetcode weekly contest 222
Runtime: 152 ms, faster than 100.00% of Python3 online submissions for Maximum Units on a Truck.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Maximum Units on a Truck.
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        print(boxTypes)
        sol = 0
        for q, units in boxTypes:
            if truckSize - q >= 0:
                sol += units*q
                truckSize -= q
            else:
                sol += units*truckSize
                break
        return sol
