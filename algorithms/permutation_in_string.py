"""
Leetcode 567
O(n) runtime, O(1) space
Runtime: 68 ms, faster than 79.09% of Python3 online submissions for Permutation in String.
Memory Usage: 14.3 MB, less than 60.69% of Python3 online submissions for Permutation in String.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occs = [0]*26
        for c in s1:
            occs[ord(c)-ord('a')] += 1
        L, i = len(s1), 0
        for j, c in enumerate(s2):
            occs[ord(c)-ord('a')] -= 1
            if j-i+1 == L:
                if not any(occs):
                    return True
                occs[ord(s2[i])-ord('a')] += 1
                i += 1
        return False
