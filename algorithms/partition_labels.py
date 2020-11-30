"""
Leetcode 763
Runtime: 36 ms, faster than 83.40% of Python3 online submissions for Partition Labels.
Memory Usage: 14.2 MB, less than 44.49% of Python3 online submissions for Partition Labels.
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mp = {}
        for i, c in enumerate(S):
            mp[c] = i
        sol = []
        last = -1
        lim = 0
        for i, c in enumerate(S):
            lim = max(lim, mp[c])
            if i == lim:
                lim = 0
                sol.append(i-last)
                last = i
        return sol
