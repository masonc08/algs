"""
Leetcode 1711
Leetcode weekly contest 222
Runtime: 640 ms, faster than 100.00% of Python3 online submissions for Count Good Meals.
Memory Usage: 20.6 MB, less than 100.00% of Python3 online submissions for Count Good Meals.
"""


import collections


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        sol = 0
        pwr = 1
        mp = collections.Counter()
        for item in deliciousness:
            while pwr < item:
                pwr *= 2
            if pwr == item:
                sol += mp[item]
                sol %= 10**9+7
            sol += mp[pwr-item]
            sol %= 10**9+7
            mp[item] += 1
        return sol

            
