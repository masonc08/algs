"""
Leetcode 1049

"""


import functools


class Solution:
    """
    O(N*S) runtime, O(S) space, where S=sum(N)
    Knapsack style DP
    Runtime: 28 ms, faster than 99.59% of Python3 online submissions for Last Stone Weight II.
    Memory Usage: 14.3 MB, less than 56.46% of Python3 online submissions for Last Stone Weight II.
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for stone in stones:
            dp.update({ stone+x for x in dp })
        s = sum(stones)
        return min(abs(s-x-x) for x in dp)

    """
    O(N*S) runtime and space, where S=sum(N)
    Memoization with LRU cache
    Runtime: 68 ms, faster than 22.18% of Python3 online submissions for Last Stone Weight II.
    Memory Usage: 22.6 MB, less than 5.23% of Python3 online submissions for Last Stone Weight II.
    """
    # def lastStoneWeightII(self, stones: List[int]) -> int:
    #     @functools.lru_cache(None)
    #     def helper(cur=0, i=0):
    #         if i == len(stones):
    #             return cur if cur >= 0 else float('inf')
    #         return min(helper(cur+stones[i], i+1), helper(cur-stones[i], i+1))
    #     return helper()
