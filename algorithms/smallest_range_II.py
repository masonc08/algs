"""
Leetcode 910
December Leetcoding challenge
Runtime: 148 ms, faster than 83.93% of Python3 online submissions for Smallest Range II.
Memory Usage: 15.4 MB, less than 51.19% of Python3 online submissions for Smallest Range II.
"""


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mina, maxa = A[0], A[-1]
        sol = maxa-mina
        for i in range(len(A)-1):
            sol = min(sol, max(maxa-K, A[i]+K)-min(mina+K, A[i+1]-K))
        return sol
