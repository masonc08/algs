"""
Leetcode 43
Runtime: 120 ms, faster than 46.21% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.2 MB, less than 19.32% of Python3 online submissions for Multiply Strings.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sol = []
        for s1 in num1:
            s1 = int(s1)
            cur = []
            carry = 0
            for i in range(len(num2)-1, -1, -1):
                l1 = int(num2[i])
                prod = l1*s1+carry
                carry = prod//10
                cur.append(str(prod%10))
            if carry:
                cur.append(str(carry))
            cur.reverse()
            sol.append(''.join(cur))
        final = 0
        for i in range(len(sol)):
            final += int(int(sol.pop())*(10**i))
        return str(final)
