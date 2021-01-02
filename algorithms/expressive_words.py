"""
Leetcode 809
Runtime: 52 ms, faster than 65.02% of Python3 online submissions for Expressive Words.
Memory Usage: 14.4 MB, less than 45.77% of Python3 online submissions for Expressive Words.
"""


class Solution:
    def expressiveWords(self, S, words):
        compressed = self.get_compressed(S)
        sol = len(words)
        for word in words:
            other = self.get_compressed(word)
            if len(other) != len(compressed):
                sol -= 1
                continue
            for (c1, occ1), (c2, occ2) in zip(compressed, other):
                if c1 != c2 or occ2 > occ1 or occ1 == 2 and occ2 == 1:
                    sol -= 1
                    break
        return sol
                

    def get_compressed(self, S):
        compressed = []
        j = 0
        for i in range(1, len(S)+1):
            if i == len(S) or S[i] != S[j]:
                compressed += (S[j], i-j),
                j = i
        return compressed
