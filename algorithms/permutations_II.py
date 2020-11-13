"""
Leetcode 47
Novemeber Leetcoding challenge
"""


from typing import List
import collections

class Solution:
    """
    Converting to counter
    Runtime: 60 ms, faster than 51.50% of Python3 online submissions for Permutations II.
    Memory Usage: 14.2 MB, less than 79.78% of Python3 online submissions for Permutations II.
    """
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     sol = []
    #     self._permuteUnique(collections.Counter(nums), [], sol, len(nums))
    #     return sol

    # def _permuteUnique(self, ctr, cur, sol, cap):
    #     if len(cur) == cap:
    #         sol.append(cur.copy())
    #     for num in ctr:
    #         if ctr[num] > 0:
    #             cur.append(num)
    #             ctr[num] -= 1
    #             self._permuteUnique(ctr, cur, sol, cap)
    #             cur.pop()
    #             ctr[num] += 1

    """
    Runtime: 60 ms, faster than 51.50% of Python3 online submissions for Permutations II.
    Memory Usage: 14.3 MB, less than 51.19% of Python3 online submissions for Permutations II.
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        sol, cur, visited = [], [], set()
        appended = set()
        for i, num in enumerate(nums):
            if num in appended:
                continue
            appended.add(num)
            cur.append(num)
            visited.add(i)
            self._permuteUnique(nums, sol, cur, visited)
            cur.pop()
            visited.remove(i)
        return sol

    def _permuteUnique(self, nums, sol, cur, visited):
        if len(cur) == len(nums):
            sol.append(cur.copy())
            return
        appended = set()
        for i, num in enumerate(nums):
            if i in visited or num in appended:
                continue
            appended.add(num)
            cur.append(num)
            visited.add(i)
            self._permuteUnique(nums, sol, cur, visited)
            cur.pop()
            visited.remove(i)
