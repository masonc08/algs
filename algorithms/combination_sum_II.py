"""
Leetcode 40
Runtime: 44 ms, faster than 90.50% of Python3 online submissions for Combination Sum II.
Memory Usage: 14.1 MB, less than 42.91% of Python3 online submissions for Combination Sum II.
"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol, cur = [], []
        def _combinationSum2(start, ttl):
            if ttl == target:
                sol.append(cur.copy())
                return
            for j in range(start+1, len(candidates)):
                new = candidates[j]
                if j != start+1 and new == candidates[j-1]:
                    continue
                if ttl+new > target:
                    break
                cur.append(new)
                _combinationSum2(j, ttl+new)
                cur.pop()

        for i in range(len(candidates)):
            v = candidates[i]
            if i != 0 and v == candidates[i-1]:
                continue
            if v > target:
                break
            cur.append(v)
            _combinationSum2(i, v)
            cur.pop()
        return sol