"""
Leetcode 6
Runtime: 72 ms, faster than 37.29% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.1 MB, less than 5.07% of Python3 online submissions for ZigZag Conversion.
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        sol = []
        i = 0
        down = 2*(numRows-1)
        up = 0
        while numRows != 0:
            j = i
            direction = "down"
            while j < len(s):
                if direction == "down":
                    if down != 0:
                        sol.append(s[j])
                        j += down
                else:
                    if up != 0:
                        sol.append(s[j])
                        j += up
                direction = "down" if direction == "up" else "up"
            down -= 2
            up += 2
            i += 1
            numRows -= 1
        return ''.join(sol)
