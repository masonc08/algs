"""
Leetcode 367
Runtime: 20 ms, faster than 98.01% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 14.1 MB, less than 56.59% of Python3 online submissions for Valid Perfect Square.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num//2+1
        while lo <= hi:
            mid = (lo+hi)//2
            cur = mid*mid
            if cur == num:
                return True
            elif cur < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
