"""
Leetcode 39
"""

# TODO: consider reviewing combo sum problems
class Solution:
    """
    Recursive approach
    Runtime: 52 ms, faster than 91.20% of Python3 online submissions for Combination Sum.
    Memory Usage: 14.1 MB, less than 7.21% of Python3 online submissions for Combination Sum.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol, cur = [], []
        def _combinationSum(rem, start=0):
            for i in range(start, len(candidates)):
                v = candidates[i]
                cur.append(v)
                if rem-v <= 0:
                    if rem-v == 0:
                        sol.append(cur.copy())
                    cur.pop()
                    break
                else:
                    _combinationSum(rem-v, i)
                cur.pop()   
        _combinationSum(target)
        return sol

    """
    Dynamic programming approach
    Runtime: 48 ms, faster than 96.11% of Python3 online submissions for Combination Sum.
    Memory Usage: 14.4 MB, less than 7.14% of Python3 online submissions for Combination Sum
    """
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates.sort()
    #     dp = [[] for _ in range(target+1)]
    #     for i in range(1, target+1):
    #         for v in candidates:
    #             if v > i:
    #                 break
    #             if i == v:
    #                 dp[i].append([v])
    #             else:
    #                 for sol in dp[i-v]:
    #                     if v >= sol[-1]:
    #                         tmp = sol.copy()
    #                         tmp.append(v)
    #                     dp[i].append(tmp)
    #     return dp[-1]
