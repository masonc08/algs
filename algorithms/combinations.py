"""
Leetcode 77
Runtime: 80 ms, faster than 92.52% of Python3 online submissions for Combinations.
Memory Usage: 15.7 MB, less than 50.59% of Python3 online submissions for Combinations.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, cur = [], []
        def helper(k, s=1):
            if k == 0:
                sol.append(cur.copy())
                return
            for i in range(s, n-k+2):
                cur.append(i)
                helper(k-1, i+1)
                cur.pop()
        helper(k)
        return sol
