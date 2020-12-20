"""
Leetcode 1694
Leetcode weekly contest 220
Runtime: 32 ms, faster than 75.00% of Python3 online submissions for Reformat Phone Number.
Memory Usage: 14.4 MB, less than 50.00% of Python3 online submissions for Reformat Phone Number.
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")
        sol = []
        for i in range(0, len(number), 3):
            if i >= len(number)-4:
                diff = len(number)-i
                if diff == 4:
                    sol += number[i:i+2],
                    sol += '-',
                    sol += number[i+2:i+4],
                else:
                    sol += number[i:i+4]
                break
            sol += number[i:i+3],
            if i+3 != len(number):
                sol += '-',
        return ''.join(sol)
