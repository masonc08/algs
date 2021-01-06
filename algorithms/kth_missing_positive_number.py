"""
Leetcode 1539
January Leetcoding challenge
Runtime: 52 ms, faster than 64.07% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14.4 MB, less than 35.70% of Python3 online submissions for Kth Missing Positive Number.
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L = len(arr)
        i, j = 0, L
        while i < j:
            m = (i+j)//2
            v = arr[m]-m-1
            if v < k:
                i = m+1
            else:
                j = m
        if i == L:
            return i+k
        v = arr[i]-i-1
        diff = v-k
        return arr[i]-diff-1
