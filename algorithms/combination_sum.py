"""
Leetcode 39
Runtime: 48 ms, faster than 96.11% of Python3 online submissions for Combination Sum.
Memory Usage: 14.4 MB, less than 7.14% of Python3 online submissions for Combination Sum."""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[] for _ in range(target+1)]
        for i in range(1, target+1):
            for v in candidates:
                if v > i:
                    break
                if i == v:
                    dp[i].append([v])
                else:
                    for sol in dp[i-v]:
                        if v >= sol[-1]:
                            tmp = sol.copy()
                            tmp.append(v)
                        dp[i].append(tmp)
        return dp[-1]
