"""
Leetcode 89
Runtime: 20 ms, faster than 99.74% of Python3 online submissions for Gray Code.
Memory Usage: 14.6 MB, less than 28.87% of Python3 online submissions for Gray Code.
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        sol = [0]
        for i in range(1, n+1):
            for j in range(len(sol)-1, -1, -1):
                sol += (sol[j] | 1<<(i-1)),
        return sol
