"""
Leetcode 227
November Leetcoding challenge
"""


class Solution:
    def calculate(self, s: str) -> int:
        sol = cur = last = 0
        last_op = "+"
        for i, c in enumerate(s):
            if c.isnumeric():
                cur *= 10
                cur += int(c)
            elif c != " " or i == len(s)-1:
                if last_op == "*":
                    prev *= cur
                elif last_op == "/":
                    prev //= cur
                else:
                    sol += prev
                    prev = cur if last_op == '+' else -cur
                last_op = c
                cur = 0
        return sol+last


    """
    O(n) runtime and space solution, two passing using a stack
    Runtime: 100 ms, faster than 37.79% of Python3 online submissions for Basic Calculator II.
    Memory Usage: 16 MB, less than 31.87% of Python3 online submissions for Basic Calculator II.
    """
    # def calculate(self, s: str) -> int:
    #     components = []
    #     cur = 0
    #     for c in s:
    #         if c.isnumeric():
    #             cur *= 10
    #             cur += int(c)
    #         elif c != " ":  # If c is one of the operations
    #             if len(components) != 0 and (components[-1] == "*" or components[-1] == "/"):
    #                 op = components.pop()
    #                 a = components.pop()
    #                 b = cur
    #                 if op == "*":
    #                     components.append(a*b)
    #                 else:
    #                     components.append(a//b)
    #             else:
    #                 components.append(cur)
    #             components.append(c)
    #             cur = 0
    #     if len(components) == 0 or not str(components[-1]).isnumeric():
    #         if len(components) != 0 and (components[-1] == "*" or components[-1] == "/"):
    #             op = components.pop()
    #             a = components.pop()
    #             b = cur
    #             if op == "*":
    #                 components.append(a*b)
    #             else:
    #                 components.append(a//b)
    #         else:
    #             components.append(cur)
    #     sol = 0
    #     cur = [0, False]
    #     for component in components:
    #         if component == "+" or component == "-":
    #             if cur[1]:
    #                 sol -= cur[0]
    #             else:
    #                 sol += cur[0]
    #             cur = [0, component == "-"]
    #         else:
    #             cur[0] = component
    #     if str(components[-1]).isnumeric():
    #         if cur[1]:
    #             sol -= cur[0]
    #         else:
    #             sol += cur[0]
    #     return sol
