"""
Leetcode 215
Runtime: 1188 ms, faster than 12.53% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 118 MB, less than 5.60% of Python3 online submissions for Kth Largest Element in an Array.
O(n) amortized runtime, O(n) space
January Leetcoding challenge
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        return self._findKthLargest(nums, k)


    def _findKthLargest(self, nums: List[int], k: int, start=0) -> int:
        if len(nums) == 1:
            return nums[0]
        pivot = nums[-1]
        i, j = 0, len(nums) - 1
        while 1:
            while nums[i] < pivot and i != j:
                i += 1
            while nums[j] >= pivot and i != j:
                j -= 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                nums[i], nums[-1] = nums[-1], nums[i]
                if start + i < k - 1:
                    return self._findKthLargest(nums[i+1:], k, start+i+1)
                elif start + i > k - 1:
                    return self._findKthLargest(nums[:i], k, start)
                else:
                    return nums[i]
