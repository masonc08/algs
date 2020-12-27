"""
Leetcode 324

"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        up = True
        for i in range(len(nums)-1):
            if up and nums[i] > nums[i+1] or not up and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif nums[i] == nums[i+1]:
                j = i+1
                if up:
                    prev = float('-inf') if i == 0 else nums[i-1]
                    while j < len(nums) and (nums[j] < prev or nums[j] >= nums[i]) and nums[j] <= nums[i+1]:
                        j += 1
                    if nums[j] > nums[i+1]:
                        nums[j], nums[i+1] = nums[i+1], nums[j]
                    elif nums[j] < nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                else:
                    prev  = float('inf') if i == 0 else nums[i-1]
                    while j < len(nums) and (nums[j] > prev or nums[j] <= nums[i]) and nums[j] >= nums[i+1]:
                        j += 1
                    if nums[j] < nums[i+1]:
                        nums[j], nums[i+1] = nums[i+1], nums[j]
                    elif nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
            up = not up


    """
    Pythonic way, O(nlogn) runtime, O(n) space
    Runtime: 164 ms, faster than 75.03% of Python3 online submissions for Wiggle Sort II.
    Memory Usage: 17.1 MB, less than 55.92% of Python3 online submissions for Wiggle Sort II.
    """
    # def wiggleSort(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()
    #     mid = len(nums[::2])
    #     nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]