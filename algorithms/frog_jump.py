"""
Leetcode 403
O(n^2) runtime and space
Runtime: 200 ms, faster than 67.64% of Python3 online submissions for Frog Jump.
Memory Usage: 15.9 MB, less than 87.48% of Python3 online submissions for Frog Jump.
"""


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 0:
            return True
        mp = { stone: set() for stone in stones }
        mp[0].add(1)
        for stone in stones:
            for jump in mp[stone]:
                dist = stone+jump
                if dist == stones[-1]:
                    return True
                if dist in mp:
                    mp[dist].add(jump+1)
                    mp[dist].add(jump)
                    jump-1 > 0 and mp[dist].add(jump-1)
        return False


# class Solution:
#     def canCross(self, stones) -> bool:
#         if stones[1] != 1:
#             return False
#         L = len(stones)
#         mp = { v:i for i, v in enumerate(stones) }
#         dp = [[False]*L for _ in range(L)]
#         for j in range(L-1, 0, -1):
#             v = stones[j]
#             for i in range(1, L):
#                 if j == L-1:
#                     dp[i][j] = True
#                     continue
#                 dp[i][j] = any(dp[i1][mp[v+i1]] for i1 in (i-1, i, i+1) if v+i1 in mp and i1 < L)
#         return dp[1][1]
