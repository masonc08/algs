"""
Leetcode 1716
Leetcode biweekly contest 43
O(1) math solution
Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Calculate Money in Leetcode Bank.
Memory Usage: 14.2 MB, less than 75.00% of Python3 online submissions for Calculate Money in Leetcode Bank.
"""


# class Solution:
#     def totalMoney(self, n: int) -> int:
#         sol = 0
#         i = 0
#         while n >= 0:
#             if n >= 7:
#                 sol += 28
#                 sol += i*7
#             else:
#                 sol += n*(n+1)//2
#                 sol += i*n
#             i += 1
#             n -= 7
#         return sol

class Solution:
    def totalMoney(self, n: int) -> int:
        w, r = n//7, n%7
        return int(w*(3.5*w+24.5)+r*(w+0.5*r+0.5))