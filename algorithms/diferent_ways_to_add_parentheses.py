"""
Leetcode 241
O(C_n) runtime, O(NN) space, where C_n is the n-th Catalan number
Runtime: 44 ms, faster than 26.08% of Python3 online submissions for Different Ways to Add Parentheses.
Memory Usage: 14.5 MB, less than 20.08% of Python3 online submissions for Different Ways to Add Parentheses.
"""


import re
import operator
import functools


class Solution:
    compute = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul
    }

    def diffWaysToCompute(self, eqn: str) -> List[int]:
        eqn = re.split(r"(\D)", eqn)
        @functools.lru_cache(None)
        def explore(s, e):
            if s == e:
                return [int(eqn[s])]
            return [
                self.compute[eqn[i+1]](lv, rv)
                for i in range(s, e-1, 2)
                for lv in explore(s, i)
                for rv in explore(i+2, e)
            ]
        return explore(0, len(eqn)-1)
