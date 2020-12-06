"""
Leetcode 852
"""


class Solution:
    """
    Runtime: 104 ms, faster than 5.91% of Python3 online submissions for Peak Index in a Mountain Array.
    Memory Usage: 15.4 MB, less than 16.09% of Python3 online submissions for Peak Index in a Mountain Array.
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 1, len(arr)-2
        while i <= j:
            m = (i+j)//2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m] < arr[m+1]:
                i = m+1
            else:
                j = m-1
        raise Exception("No solution")
 

    """
    O(n) runtime, O(1) space by linear scanning
    Runtime: 108 ms, faster than 5.91% of Python3 online submissions for Peak Index in a Mountain Array.
    Memory Usage: 15.3 MB, less than 34.62% of Python3 online submissions for Peak Index in a Mountain Array.
    """
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     sol = 0
    #     for i in range(len(arr)):
    #         sol = max(sol, i, key=lambda x: arr[x])
    #     return sol
