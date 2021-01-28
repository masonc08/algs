"""
Leetcode 415
O(n) runtime and space
Runtime: 48 ms, faster than 42.84% of Python3 online submissions for Add Strings.
Memory Usage: 14.6 MB, less than 24.26% of Python3 online submissions for Add Strings.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        L1, L2 = len(num1)-1, len(num2)-1
        i, j, sol, c = L1, L2, [], 0
        while i >= 0 or j >= 0 or c:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            n = a+b+c
            c, n = n//10, n%10
            sol.append(str(n))
            i, j = i-1, j-1 
        return ''.join(sol[::-1])
