"""
Leetcode 833
Runtime: 36 ms, faster than 73.59% of Python3 online submissions for Find And Replace in String.
Memory Usage: 14.4 MB, less than 21.83% of Python3 online submissions for Find And Replace in String.
"""


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        sol = list(S)
        for i, source, target in zip(indexes, sources, targets):
            L = len(source)
            if S[i:i+L] != source:
                continue
            sol[i:i+L] = ['']*L
            sol[i] = target
        return ''.join(sol)
