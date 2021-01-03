"""
Leetcode 1296, 846
"""


import collections


class Solution:
    """
    O(n) runtime, O(m) space by identifying streak roots
    Runtime: 468 ms, faster than 32.91% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
    Memory Usage: 28.8 MB, less than 57.24% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
    """
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        L = len(nums)
        if L%k != 0:
            return False
        ct = collections.Counter(nums)
        for start in nums:
            cur = start
            while cur <= start:
                while ct[cur-1] != 0:
                    cur -= 1
                occ = ct[cur]
                if occ:
                    for i in range(k):
                        ct[cur+i] -= occ
                        if ct[cur+i] < 0:
                            return False
                cur += 1
        return True
    """
    O(mlogm) runtime, O(m) space by sorting
    Runtime: 380 ms, faster than 97.64% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
    Memory Usage: 28.8 MB, less than 57.24% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
    """
    # def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    #     L = len(nums)
    #     if L%k != 0:
    #         return False
    #     ct = collections.Counter(nums)
    #     for n in sorted(ct):
    #         if ct[n] > 0:
    #             occ = ct[n]
    #             for i in range(k):
    #                 ct[n+i] -= occ
    #                 if ct[n+i] < 0:
    #                     return False
    #     return True
