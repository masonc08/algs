"""
Databricks OA

Problem:
Given an array of integers A, return the number of pairs (i, j) which satisfy the following conditions:
- i <= j
- A[i] + rev(A[j]) == A[j] + rev(A[i]), where rev() takes an integer, and returns a reversed version of the integer.
  - Examples of the rev() function:
      rev(512512) == 215215
      rev(12345) == 54321
      rev(1) == 1

Eg:
[1, 20, 2, 11] -> 7
  Reasoning:
  (1, 1) satisfies both conditions
  (1, 2) satisfies both conditions
  (1, 11) satisfies both conditions
  (20, 20) satisfies both conditions
  (2, 2) satisfies both conditions
  (2, 11) satisfies both conditions
  (11, 11) satisfies both conditions
  There are a total of 7 (i, j) pairs, thus the solution to this problem is 7.
"""


import collections


class Solution:
    def reverse_sum_pair(self, nums: list) -> int:
        mp = collections.defaultdict(int)
        sol = len(nums)
        for num in nums:
            diff = num-self._reverse(num)
            sol += mp[diff]
            mp[diff] += 1
        return sol

    def _reverse(self, num: int) -> int:
        sol = 0
        while num:
            sol *= 10
            sol += num%10
            num //= 10
        return sol

f = Solution().reverse_sum_pair
rev = Solution()._reverse

assert rev(512512) == 215215
assert rev(12345) == 54321
assert rev(1) == 1
assert f([1, 20, 2, 11]) == 7
assert f([1, 2, 3, 4]) == 10
assert f([0]) == 1
