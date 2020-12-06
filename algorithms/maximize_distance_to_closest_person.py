"""
Leetcode 849
Runtime: 248 ms, faster than 5.60% of Python3 online submissions for Maximize Distance to Closest Person.
Memory Usage: 14.9 MB, less than 10.47% of Python3 online submissions for Maximize Distance to Closest Person.
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        b = seats.index(1)
        a = -b
        sol = (b-a)//2
        for i in range(b+1, len(seats)):
            if seats[i] == 1:
                a, b = b, i
                sol = max(sol, (b-a)//2)
            elif i == len(seats)-1:
                sol = max(sol, i-b)
        return sol
