"""
Leetcode 474
"""


import collections


"""
Runtime: 5044 ms, faster than 25.88% of Python3 online submissions for Ones and Zeroes.
Memory Usage: 14.4 MB, less than 92.21% of Python3 online submissions for Ones and Zeroes.
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            ct = collections.Counter(s)
            for i in range(m, ct['0']-1, -1):
                for j in range(n, ct['1']-1, -1):
                    dp[i][j] = max(dp[i-ct['0']][j-ct['1']]+1, dp[i][j])
        return dp[m][n]


    """
    Solution using hashmap for dp
    Runtime: 2280 ms, faster than 88.06% of Python3 online submissions for Ones and Zeroes.
    Memory Usage: 14.6 MB, less than 59.20% of Python3 online submissions for Ones and Zeroes.
    """
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     L = len(strs)
    #     ct = [(0,0)]*L
    #     for i in range(L):
    #         ct[i] = strs[i].count('0'), strs[i].count('1')
    #     dp = {(m, n): 0}
    #     sol = 0
    #     for zeroes, ones in ct:
    #         new = {}
    #         for a, b in dp:
    #             if a-zeroes >= 0 and b-ones >= 0:
    #                 cur = max(dp[(a,b)]+1, dp.get((a-zeroes, b-ones), 0))
    #                 sol = max(sol, cur)
    #                 new[(a-zeroes, b-ones)] = cur
    #         dp.update(new)
    #     return sol
