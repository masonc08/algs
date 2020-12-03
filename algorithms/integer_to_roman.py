"""
Leetcode 12
"""


import math


class Solution:
    """
    Runtime: 44 ms, faster than 81.67% of Python3 online submissions for Integer to Roman.
    Memory Usage: 14.1 MB, less than 90.67% of Python3 online submissions for Integer to Roman.
    """
    def intToRoman(self, num: int) -> str:
        sol = [
            self.M[num//1000],
            self.C[(num%1000)//100],
            self.X[(num%100)//10],
            self.I[num%10]
        ]
        return ''.join(sol)

    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


    """
    Runtime: 64 ms, faster than 9.54% of Python3 online submissions for Integer to Roman.
    Memory Usage: 14.1 MB, less than 62.93% of Python3 online submissions for Integer to Roman.
    """
    # def intToRoman(self, num: int) -> str:
    #     sol = []
    #     s = int(math.log10(num))+1
    #     while s:
    #         first = int(num//10**(s-1))
    #         n = int(first*(10**(s-1)))
    #         if n in self.MP:
    #             sol.append(self.MP[n])
    #         else:
    #             if first > 5:
    #                 sol += [self.MP[int(5*(10**(s-1)))]]
    #                 sol += [self.MP[int(10**(s-1))]]*(first-5)
    #             elif first < 5:
    #                 sol += [self.MP[int(10**(s-1))]]*(first)
    #         num -= n
    #         s -= 1
    #     return ''.join(sol)

    # MP = {
    #     1: "I",
    #     4: "IV",
    #     5: "V",
    #     9: "IX",
    #     10: "X",
    #     40: "XL",
    #     50: "L",
    #     90: "XC",
    #     100: "C",
    #     400: "CD",
    #     500: "D",
    #     900: "CM",
    #     1000: "M"
    # }
