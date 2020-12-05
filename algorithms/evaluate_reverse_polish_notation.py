"""
Leetcode 150
Runtime: 76 ms, faster than 17.51% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.7 MB, less than 59.97% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""


class Solution:

    def _is_numeric(self, s):
        try:
            int(s)
        except ValueError:
            return False
        return True


    def evalRPN(self, tokens: List[str]) -> int:
        compute = {
            '+': lambda a, b: int(a)+int(b),
            '-': lambda a, b: int(a)-int(b),
            '*': lambda a, b: int(a)*int(b),
            '/': lambda a, b: int(int(a)/int(b))
        }
        stk = []
        for token in tokens:
            if self._is_numeric(token):
                stk.append(token)
            else:
                b = stk.pop()
                a = stk.pop()
                stk.append(compute[token](a, b))
        return stk[0]
