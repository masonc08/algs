"""
Leetcode 4
"""


"""
O(log(m+n)) runtime, O(1) space
Runtime: 92 ms, faster than 69.61% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.7 MB, less than 26.86% of Python3 online submissions for Median of Two Sorted Arrays.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        nums1, nums2 = sorted((nums1, nums2), key=len, reverse=True)
        L1, L2 = len(nums1), len(nums2)
        L = L1+L2
        s, e = 0, L1
        while s <= e:
            m1 = (s+e)//2
            m2 = L//2-m1
            m1l, m1r = float('-inf') if m1 == 0 else nums1[m1-1], nums1[m1] if m1 < L1 else float('inf')
            m2l, m2r = float('-inf') if m2 == 0 else nums2[m2-1], nums2[m2] if m2 < L2 else float('inf')
            if m1l <= m2r and m2l <= m1r:
                return min(m1r, m2r) if L%2 == 1 else (max(m1l, m2l)+min(m1r, m2r))/2
            if m1l > m2r:
                e = m1-1
            else:
                s = m1+1
        return s

"""
O(N+M) runtime, O(1) space
Runtime: 104 ms, faster than 24.30% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.6 MB, less than 58.34% of Python3 online submissions for Median of Two Sorted Arrays.
"""
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         L1, L2 = len(nums1), len(nums2)
#         def get_max():
#             i, j = L1-1, L2-1
#             while i >= 0 or j >= 0:
#                 if i >= 0 and (j < 0 or nums1[i] > nums2[j]):
#                     yield float(nums1[i])
#                     i -= 1
#                 else:
#                     yield float(nums2[j])
#                     j -= 1
#         sol = 0
#         gen = get_max()
#         for _ in range((L1+L2)//2+(L1+L2)%2):
#             sol = next(gen)
#         if (L1+L2)%2 == 0:
#             temp = next(gen)
#             sol = (sol+temp)/2
#         return sol
