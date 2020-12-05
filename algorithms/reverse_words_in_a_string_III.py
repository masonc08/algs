"""
Leetcode 557
"""


import collections


class Solution:
    """
    Using builtins
    Runtime: 32 ms, faster than 72.70% of Python3 online submissions for Reverse Words in a String III.
    Memory Usage: 14.6 MB, less than 95.80% of Python3 online submissions for Reverse Words in a String III.
    """
    def reverseWords(self, s: str) -> str:
        return ' '.join([ word[::-1] for word in s.split() ])


    """
    Using stack
    Runtime: 64 ms, faster than 19.87% of Python3 online submissions for Reverse Words in a String III.
    Memory Usage: 14.8 MB, less than 59.58% of Python3 online submissions for Reverse Words in a String III.
    """
    # def reverseWords(self, s: str) -> str:
    #     sol = []
    #     stk = collections.deque()
    #     for c in s:
    #         if c == '':
    #             sol.append(''.join(stk))
    #             stk = collections.deque()
    #         else:
    #             stk.appendleft(c)
    #     return ' '.join(sol)
