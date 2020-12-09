"""
Leetcode 28
Runtime: 52 ms, faster than 6.36% of Python3 online submissions for Implement strStr().
Memory Usage: 15.7 MB, less than 5.38% of Python3 online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        table = [0]*len(needle)
        i, j = 0, 1
        while j < len(needle):
            if needle[j] == needle[i]:
                i += 1
                table[j] = i
                j += 1
            elif i == 0:
                j += 1
            else:
                i = table[i-1]
        i, j = 0, 0
        while j < len(haystack):
            c = haystack[j]
            if c == needle[i]:
                i += 1
                j += 1
            elif i != 0:
                i = table[i-1]
            else:
                j += 1
            if i >= len(needle):
                return j-len(needle)
        return -1
