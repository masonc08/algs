"""
Leetcode 231
"""


class Solution:
    """
    O(1) space and runtime by using n&(n-1) to detect last bit
    Runtime: 48 ms, faster than 7.62% of Python3 online submissions for Power of Two.
    Memory Usage: 14 MB, less than 79.25% of Python3 online submissions for Power of Two.
    """
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not n-(n&(-n))


    """
    O(32) runtime, O(1) space by scanning for a single 1-bit
    Runtime: 44 ms, faster than 7.62% of Python3 online submissions for Power of Two.
    Memory Usage: 14.1 MB, less than 79.25% of Python3 online submissions for Power of Two.
    """
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while n:
    #         lsb = n&1
    #         n >>= 1
    #         if lsb == 1:
    #             return n == 0
    #     return True
