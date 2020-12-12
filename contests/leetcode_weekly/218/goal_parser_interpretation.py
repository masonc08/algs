"""
Leetcode 1678
Leetcode contest 218
Runtime: 40 ms, faster than 25.00% of Python3 online submissions for Goal Parser Interpretation.
Memory Usage: 14.3 MB, less than 25.00% of Python3 online submissions for Goal Parser Interpretation.
"""


class Solution:
    # Regex replacing
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

    # Counting
    # def interpret(self, command: str) -> str:
    #     sol = []
    #     i = 0
    #     while i < len(command):
    #         if i < len(command)-3 and command[i:i+4] == "(al)":
    #             sol.append("al")
    #             i += 4
    #         elif i < len(command)-1 and command[i:i+2] == "()":
    #             sol.append("o")
    #             i += 2
    #         else:
    #             sol.append("G")
    #             i += 1
    #     return ''.join(sol)
