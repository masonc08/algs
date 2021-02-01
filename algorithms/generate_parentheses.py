"""
Leetcode 22

"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur, sol = [], []
        def gen(op, cl):
            if len(cur) == n+n:
                sol.append(''.join(cur))
                return
            if op < n:
                cur.append('(')
                gen(op+1, cl)
                cur.pop()
            if op > cl:
                cur.append(')')
                gen(op, cl+1)
                cur.pop()
        gen(0, 0)
        return sol
