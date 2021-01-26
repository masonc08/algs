"""
Leetcode 388
O(n) runtime and space
Runtime: 24 ms, faster than 92.97% of Python3 online submissions for Longest Absolute File Path.
Memory Usage: 14.1 MB, less than 96.68% of Python3 online submissions for Longest Absolute File Path.
"""


class Solution:
    def lengthLongestPath(self, s: str) -> int:
        mp = {0: 0}
        sol = 0
        for name in s.splitlines():
            cleaned = name.lstrip('\t')
            d = len(name)-len(cleaned)
            if '.' in cleaned:
                sol = max(sol, mp[d]+len(cleaned))
            else:
                mp[d+1] = mp[d]+len(cleaned)+1
        return sol
