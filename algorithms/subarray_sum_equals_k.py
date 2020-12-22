"""
Leetcode 560
Runtime: 268 ms, faster than 24.29% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 16.8 MB, less than 24.07% of Python3 online submissions for Subarray Sum Equals K.
"""

class Solution:
    def subarraySum(self, A: List[int], S: int) -> int:
        mp = collections.Counter()
        mp[0] = 1
        cur = 0
        sol = 0
        for n in A:
            cur += n
            if cur-S in mp:
                sol += mp[cur-S]
            mp[cur] += 1
        return sol
