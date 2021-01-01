"""
Leetcode 1640
January Leetcoding challenge
Runtime: 40 ms, faster than 72.47% of Python3 online submissions for Check Array Formation Through Concatenation.
Memory Usage: 14.3 MB, less than 14.54% of Python3 online submissions for Check Array Formation Through Concatenation.
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {}
        for i, piece in enumerate(pieces):
            mp[piece[0]] = i
        i = 0
        while i < len(arr):
            if arr[i] not in mp:
                return False
            w = pieces[mp[arr[i]]]
            j = 0
            while i < len(arr) and j < len(w) and arr[i] == w[j]:
                i += 1
                j += 1
            if j != len(w):
                return False
        return True
