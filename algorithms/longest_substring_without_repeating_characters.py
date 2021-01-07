"""
Leetcode 3
January Leetcoding challenge
Runtime: 60 ms, faster than 73.51% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 75.40% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        j = sol = 0
        seen = {}
        for i in range(L):
            c = s[i]
            if c in seen:
                while s[j] != c:
                    del seen[s[j]]
                    j += 1
                del seen[s[j]]
                j += 1
            seen[c] = True
            sol = max(sol, i-j+1)
        return sol
