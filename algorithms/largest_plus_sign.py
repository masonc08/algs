"""
Leetcode 764

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n]*n for  _ in range(n)]
        for i, j in mines:
            dp[i][j] = 0
        def populate(iter1, iter2, rows=True, rev=False):
            for i in iter1:
                cur = 0
                for j in range(iter2-1, -1, -1) if rev else range(iter2):
                    if rows:
                        cur = cur+1 if dp[i][j] != 0 else 0
                        dp[i][j] = min(dp[i][j], cur)
                    else:
                        cur = cur+1 if dp[j][i] != 0 else 0
                        dp[j][i] = min(dp[j][i], cur)

        populate(range(n), n)
        populate(range(n), n, True, True)
        populate(range(n), n, False)
        populate(range(n), n, False, True)
        return max(map(max, dp))
