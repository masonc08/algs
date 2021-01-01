"""
Leetcode 524
Runtime: 548 ms, faster than 42.11% of Python3 online submissions for Longest Word in Dictionary through Deleting.
Memory Usage: 16.9 MB, less than 28.94% of Python3 online submissions for Longest Word in Dictionary through Deleting.
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        sol = ""
        for w in d:
            if self.is_subsequence(s, w):
                sol = sorted([sol, w], key=lambda x: (-len(x), x))[0]
        return sol

    def is_subsequence(self, s, w):
        i = 0
        for c1 in s:
            if i < len(w) and c1 == w[i]:
                i += 1
            if i == len(w):
                return True
        return False
