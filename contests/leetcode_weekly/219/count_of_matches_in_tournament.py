"""
Leetcode 1688
Leetcode weekly contst 219
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Count of Matches in Tournament.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Count of Matches in Tournament.
"""

# Can also solve simply by returning n-1


class Solution:
    def numberOfMatches(self, n: int) -> int:
        sol = 0
        while n != 1:
            if n%2 == 0:
                n //= 2
                sol += n
            else:
                n //= 2
                sol += n
                n += 1
        return sol
