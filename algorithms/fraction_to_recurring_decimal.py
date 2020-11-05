"""
Leetcode 116
Runtime: 28 ms, faster than 79.54% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator == 0:
            return str(numerator//denominator)
        negative = (numerator < 0) ^ (denominator < 0)
        sol = []
        negative and sol.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        sol.append(str(numerator//denominator))
        sol.append('.')
        numerator %= denominator
        seen = {}
        tmp = numerator//denominator
        while 1:
            numerator *= 10
            tmp = numerator//denominator
            sol.append(str(tmp))
            numerator -= tmp*denominator
            if numerator == 0:
                return ''.join(sol)
            if (tmp, numerator) in seen:
                break
            seen[(tmp, numerator)] = len(sol)
        left_bracket = seen[(tmp, numerator)]-1
        sol.insert(left_bracket, '(')
        sol[-1] = ')'
        return ''.join(sol)
