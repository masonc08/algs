"""
Leetcode 88
Runtime: 36 ms, faster than 66.08% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        i = len(nums1)-1
        while n > -1:
            if m == -1 or nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1
            i -= 1
