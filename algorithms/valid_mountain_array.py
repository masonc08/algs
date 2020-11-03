"""
Leetcode 941
Runtime: 184 ms, faster than 98.35% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Valid Mountain Array.
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        increased = False
        decreasing = False
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                increased = True
                if decreasing:
                    return False
            elif A[i] > A[i+1]:
                if not decreasing:
                    decreasing = True
            else:
                return False
        return increased and decreasing
