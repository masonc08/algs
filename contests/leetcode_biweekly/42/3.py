"""
Leetcode 1703
Leetcode biweekly contest 42
Runtime: 280 ms, faster than 33.33% of Python3 online submissions for Maximum Binary String After Change.
Memory Usage: 17.1 MB, less than 33.33% of Python3 online submissions for Maximum Binary String After Change.
"""


import collections


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        sol = []
        i = binary.find('0')
        if i == -1:
            return binary
        sol += binary[:i]
        ct = collections.Counter(binary[i:])
        sol += ['1']*(ct['0']-1) + ['0'] + ['1']*ct['1']
        return ''.join(sol)
