"""
Leetcode 1249
Runtime: 84 ms, faster than 94.62% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 15.9 MB, less than 80.94% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sol = list(s)
        stk = []
        for i, c in enumerate(sol):
            if c == '(':
                stk += i,
            elif c == ')':
                if not stk:
                    sol[i] = ''
                else:
                    stk.pop()
        while stk:
            sol[stk.pop()] = ''
        return ''.join(sol)
