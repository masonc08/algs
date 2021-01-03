"""
Leetcode 526
January Leetcoding challenge
Runtime: 176 ms, faster than 79.25% of Python3 online submissions for Beautiful Arrangement.
Memory Usage: 14.3 MB, less than 54.95% of Python3 online submissions for Beautiful Arrangement.
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        rem = [True]*(n+1)
        def count(n):
            if n == 0:
                return 1
            sol = 0
            for i in range(1, len(rem)):
                if rem[i] and (n%i == 0 or i%n == 0):
                    rem[i] = False
                    sol += count(n-1)
                    rem[i] = True
            return sol
        return count(n)
