"""
Leetcode 394
Runtime: 28 ms, faster than 70.42% of Python3 online submissions for Decode String.
Memory Usage: 14.3 MB, less than 5.23% of Python3 online submissions for Decode String.
"""


class Solution:
    def decodeString(self, s: str, i=0) -> str:
        sol = []
        stk = []
        i = i
        while i < len(s):
            c = s[i]
            if c.isdigit():
                digit = []
                while s[i].isdigit():
                    digit.append(s[i])
                    i += 1
                stk.append([int(''.join(digit)), []])
            elif c == ']':
                reps, frag = stk.pop()
                if stk:
                    stk[-1][1] += frag*reps
                else:
                    sol += frag*reps
            else:
                if stk:
                    stk[-1][1].append(c)
                else:
                    sol.append(c)
            i += 1
        return ''.join(sol)
