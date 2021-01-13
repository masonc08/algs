"""
Leetcode 881
January Leetcoding challenge
O(n) runtime, O(1) space
Runtime: 452 ms, faster than 63.43% of Python3 online submissions for Boats to Save People.
Memory Usage: 21 MB, less than 49.58% of Python3 online submissions for Boats to Save People.
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L = len(people)
        i, j, sol = 0, L-1, 0
        while i < j:
            if people[i]+people[j] <= limit:
                i += 1
            sol, j = sol+1, j-1
        return sol if i > j else sol+1
