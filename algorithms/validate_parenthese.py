"""
Leetcode 20
Runtime: 32 ms, faster than 55.65% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closes = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for symb in s:
            if symb not in closes:
                stk.append(symb)
            else:
                if len(stk) > 0 and stk[-1] == closes[symb]:
                    stk.pop()
                else:
                    return False
        return not stk