"""
Leetcode 387
Runtime: 96 ms, faster than 72.64% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.5 MB, less than 14.91% of Python3 online submissions for First Unique Character in a String.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
