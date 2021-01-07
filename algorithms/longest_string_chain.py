"""
Leetcode 1048
Runtime: 172 ms, faster than 45.97% of Python3 online submissions for Longest String Chain.
Memory Usage: 16.2 MB, less than 11.98% of Python3 online submissions for Longest String Chain.
"""


import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = collections.defaultdict(int)
        for word in words:
            dp[word] = max(dp[word[:i]+word[i+1:]]+1 for i in range(len(word)))
        return max(dp.values())
