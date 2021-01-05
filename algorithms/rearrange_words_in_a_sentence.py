"""
Leetcode 1451
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Rearrange Words in a Sentence.
Memory Usage: 16 MB, less than 75.94% of Python3 online submissions for Rearrange Words in a Sentence.
"""


class Solution:
    def arrangeWords(self, text: str) -> str:
        sol = list(text.lower().split(' '))
        sol.sort(key=len)
        sol[0] = sol[0].title()
        return ' '.join(sol)
