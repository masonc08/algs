"""
Leetcode 953
Runtime: 36 ms, faster than 63.07% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14.1 MB, less than 81.26% of Python3 online submissions for Verifying an Alien Dictionary.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {}
        for i, v in enumerate(order):
            idx[v] = i
        for i in range(len(words)-1):
            a, b = words[i], words[i+1]
            i = 0
            while i < min(len(a), len(b)) and idx[a[i]] == idx[b[i]]:
                i += 1
            if i == len(b) or i != len(a) and idx[a[i]] > idx[b[i]]:
                return False
        return True    