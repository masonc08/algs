"""
Leetcode 518
"""


import functools


class Solution:
    """
    O(m*n) runtime, O(m*n) space by LRU cache
    Runtime: 992 ms, faster than 11.92% of Python3 online submissions for Coin Change 2.
    Memory Usage: 320.2 MB, less than 5.02% of Python3 online submissions for Coin Change 2.
    """
    def change(self, amount: int, coins: list[int]) -> int:
        @functools.lru_cache(None)
        def helper(amount, i):
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            return helper(amount-coins[i], i) + helper(amount, i+1)
        return helper(amount, 0)

    """
    O(m*n) runtime, O(n) space, n=amount
    Runtime: 240 ms, faster than 46.70% of Python3 online submissions for Coin Change 2.
    Memory Usage: 14.5 MB, less than 60.43% of Python3 online submissions for Coin Change 2.
    """
    # def change(self, amount: int, coins: list[int]) -> int:
    #     n = amount+1
    #     sol = [0]*n
    #     sol[0] = 1
    #     for coin in coins:
    #         for i in range(1, n):
    #              sol[i] += sol[i-coin] if i-coin >= 0 else 0
    #     return sol[-1]
