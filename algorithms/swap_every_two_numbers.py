"""
Databricks OA

Problem:
Given an integer n, swap every two numbers from left to right. If the number has an odd number of digits, leave the last digit.
Eg:
12345 -> 21435
4129 -> 1492
1 -> 1
5555 -> 5555 
"""
import math


class Solution:
    def swap_every_two_numbers(self, n):
        if n == 0:
            return 0
        sol = 0
        digits = 1+int(math.log10(n))
        while digits > 1:
            first = n//(10**(digits-1))
            n %= 10**(digits-1)
            second = n//(10**(digits-2))
            n %= 10**(digits-2)
            digits -= 2
            sol *= 100
            sol += (second*10+first)
        if digits == 1:
            sol *= 10
            sol += n
        return sol

func = Solution().swap_every_two_numbers

assert func(12345) == 21435
assert func(11111111) == 11111111
assert func(0) == 0
assert func(512238) == 152283
assert func(1) == 1