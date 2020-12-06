"""
Leetcode 1160
Runtime: 180 ms, faster than 43.30% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.7 MB, less than 29.48% of Python3 online submissions for Find Words That Can Be Formed by Characters.
"""


import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sol = 0
        for word in words:
            cnt = collections.Counter(chars)
            flag = False
            for c in word:
                if not cnt[c]:
                    flag = True
                    break
                cnt[c] -= 1
            if not flag:
                sol += len(word)
        return sol
