"""
Leetcode 581
Runtime: 220 ms, faster than 40.54% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 15.3 MB, less than 45.54% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
"""


import bisect


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return 0
        i, j = 0, L-1
        while i < j and nums[i] <= nums[j] and \
            (nums[i] <= nums[i+1] or nums[j] >= nums[j-1]):
            if nums[i] <= nums[i+1]:
                i += 1
            if nums[j] >= nums[j-1]:
                j -= 1
        if j < i or i == j and i != 0 and j != L-1 and nums[i-1] <= nums[i] <= nums[i+1]:
            return 0
        ma, mi = float('-inf'), float('inf')
        for k in range(i, j+1):
            ma, mi = max(ma, nums[k]), min(mi, nums[k])
        i = bisect.bisect(nums, mi, hi=i)
        j = bisect.bisect_left(nums, ma, lo=j+1, hi=L)-1
        return j-i+1
