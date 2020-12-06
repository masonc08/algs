"""
Leetcode 179
Leetcode contest 218
Runtime: 844 ms, faster than 25.00% of Python3 online submissions for Max Number of K-Sum Pairs.
Memory Usage: 27.3 MB, less than 75.00% of Python3 online submissions for Max Number of K-Sum Pairs.
"""


import collections


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        sol = 0
        for num in nums:
            if k-num in mp:
                sol += 1
                mp[k-num] -= 1
                if mp[k-num] == 0:
                    del mp[k-num]
            else:
                mp[k-num] += 1
        return sol
