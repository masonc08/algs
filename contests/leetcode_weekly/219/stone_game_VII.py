"""
Leetcode 1690
Leetcode weekly contest 219
Runtime: 5896 ms, faster than 66.67% of Python3 online submissions for Stone Game VII.
Memory Usage: 121.5 MB, less than 33.33% of Python3 online submissions for Stone Game VII.
"""


import itertools


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[0]*len(stones) for _ in stones]
        csum = [0] + list(itertools.accumulate(stones))
        def dfs(i=0, j=len(stones)-1):
            if i == j:
                return 0
            if dp[i][j] == 0:
               score = csum[j+1]-csum[i]
               dp[i][j] = max(score-stones[i]-dfs(i+1, j), score-stones[j]-dfs(i, j-1))
            return dp[i][j] 
        return dfs()



    # def stoneGameVII(self, stones: List[int]) -> int:
    #     i, j = 0, len(stones)-1
    #     ttl = sum(stones)
    #     a = b = 0
    #     turn = 1
    #     while 69:
    #         if turn == 1:
    #             if stones[i] < stones[j]:
    #                 ttl -= stones[i]
    #                 a += ttl
    #                 i += 1
    #             else:
    #                 ttl -= stones[j]
    #                 a += ttl
    #                 j -= 1
    #         else:
    #             if j-i+1 == 2:
    #                 b += (ttl-min(stones[i], stones[j]))
    #                 break
    #             if j-i+1 == 1:
    #                 break
    #             # bgain = ttl-stones[i]
    #             # again = ttl-stones[i]-min(stones[i+1], stones[j])
    #             # diff = bgain-again
    #             # bgain = ttl-stones[j]
    #             # again = ttl-stones[j]-min(stones[i], stones[j-1])
    #             # if bgain-again > diff:
    #             #     ttl -= stones[j]
    #             #     b += ttl
    #             #     j -= 1
    #             # else:
    #             #     ttl -= stones[i]
    #             #     b += ttl
    #             #     i += 1
    #             smallest = min(stones[i], stones[i+1], stones[j], stones[j-1])
    #             if j-i+1 == 3 and smallest == stones[i+1] == stones[j-1]:
    #                 if stones[i] < stones[j]:
    #                     ttl -= stones[i]
    #                     b += ttl
    #                     i += 1
    #                 else:
    #                     ttl -= stones[j]
    #                     b += ttl
    #                     j -= 1
    #             elif smallest in [stones[i], stones[j-1]]:
    #                 ttl -= stones[i]
    #                 b += ttl
    #                 i += 1
    #             else:
    #                 ttl -= stones[j]
    #                 b += ttl
    #                 j -= 1
    #         turn = -turn
    #     return abs(a-b)
