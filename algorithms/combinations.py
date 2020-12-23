"""
Leetcode 77
Runtime: 80 ms, faster than 92.52% of Python3 online submissions for Combinations.
Memory Usage: 15.7 MB, less than 50.59% of Python3 online submissions for Combinations.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, cur = [], []
        def helper(d, i=1):
            if d == k+1:
                sol.append(cur.copy())
                return
            for i in range(i, n-(k-d)+1):
                cur.append(i)
                helper(d+1, i+1)
                cur.pop()
        helper(1)
        return sol
