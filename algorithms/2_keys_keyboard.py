"""
Leetcode 650

"""


import functools


class Solution:
    """
    Runtime: 572 ms, faster than 20.56% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 14.1 MB, less than 75.24% of Python3 online submissions for 2 Keys Keyboard.
    """
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i%j == 0:
                    dp[i] = dp[j] + i//j
                    break
        return dp[n]

    """
    Runtime: 172 ms, faster than 38.00% of Python3 online submissions for 2 Keys Keyboard.
    Memory Usage: 33.8 MB, less than 5.06% of Python3 online submissions for 2 Keys Keyboard.
    """
    # def minSteps(self, n: int) -> int:
    #     @functools.lru_cache(None)
    #     def explore(cur, clip):
    #         if cur == n:
    #             return 0
    #         if cur > n:
    #             return float('inf')
    #         return min(explore(cur*2, cur)+2, explore(cur+clip, clip)+1 if clip != 0 else float('inf'))
    #     return explore(1, 0)
