"""
Leetcode 1734
Leetcode biweekly contest 44
O(n) runtime, O(n) space
Runtime: 1156 ms, faster than 50.00% of Python3 online submissions for Decode XORed Permutation.
Memory Usage: 34.2 MB, less than 50.00% of Python3 online submissions for Decode XORed Permutation.
"""


from itertools import accumulate
from functools import reduce
import operator


class Solution:
    def decode(self, encoded):
        L = len(encoded)
        A = reduce(operator.xor, accumulate(encoded, operator.xor))
        A ^= reduce(operator.xor, range(1, L+2))
        return accumulate([A] + encoded, operator.xor)
