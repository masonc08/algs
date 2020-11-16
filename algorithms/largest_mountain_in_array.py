"""
Leetcode 845
November Leetcoding challenge
Runtime: 148 ms, faster than 99.02% of Python3 online submissions for Longest Mountain in Array.
Memory Usage: 15 MB, less than 37.87% of Python3 online submissions for Longest Mountain in Array.
"""


from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        decreasing = True
        i = -1
        sol = 0
        last = A[0]
        for j in range(1, len(A)):
            v = A[j]
            if v > last:
                if decreasing:
                    if i != -1:
                        sol = max(sol, j-i)
                    i = j-1
                    decreasing = False
            elif v < last:
                decreasing = True
            else:
                if decreasing and i != -1:
                    sol = max(sol, j-i)
                i = -1
                decreasing = True
            last = v
        if decreasing and i != -1:
            sol = max(sol, j-i+1)
        return sol
