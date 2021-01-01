"""
Leetcode 518
Runtime: 240 ms, faster than 46.70% of Python3 online submissions for Coin Change 2.
Memory Usage: 14.5 MB, less than 60.43% of Python3 online submissions for Coin Change 2.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount+1
        sol = [0]*n
        sol[0] = 1
        for coin in coins:
            for i in range(1, n):
                if i-coin >= 0:
                    sol[i] += sol[i-coin]
        return sol[-1]
