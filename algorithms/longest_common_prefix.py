"""
Leetcode 14
Runtime: 32 ms, faster than 78.33% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ""
        i = 0
        j = 0
        while 1:
            while i < len(strs)-1:
                if j >= len(strs[i]) or j >= len(strs[i+1]) or strs[i][j] != strs[i+1][j]:
                    return strs[i][:j]
                i += 1
            j += 1
            i = 0
            