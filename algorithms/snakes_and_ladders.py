"""
Leetcode 909
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


"""
O(n^2) runtime, O(min(6^d, n^2))
Runtime: 116 ms, faster than 73.67% of Python3 online submissions for Snakes and Ladders.
Memory Usage: 14.3 MB, less than 82.03% of Python3 online submissions for Snakes and Ladders.
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_coords(cell):
            res, mod = divmod(cell-1, n)
            return ~res, (mod if res%2 == 0 else ~mod)
        dp, stk = {1: 0}, [1]
        for cell in stk:
            for i in range(cell+1, min(cell+6, n*n)+1):
                a, b = get_coords(i)
                next_location = i if board[a][b] == -1 else board[a][b]
                if next_location == n*n:
                    return dp[cell]+1
                if next_location not in dp:
                    stk.append(next_location)
                    dp[next_location] = dp[cell]+1
        return -1
