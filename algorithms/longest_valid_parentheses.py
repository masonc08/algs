"""
Leetcode 32

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sol = 0
        stk = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            else:
                if stk[-1] != -1 and s[stk[-1]] == '(':
                    stk.pop()
                    sol = max(sol, i-stk[-1])
                else:
                    stk.append(i)
        return sol
