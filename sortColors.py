class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        a = -1
        b = len(nums)
        i = 0
        while 1:
            while i != a:
                if i == b:
                    return nums
                if nums[i] == 0:
                    a += 1
                    nums[a], nums[i] = nums[i], nums[a]
                elif nums[i] == 1:
                    break
                elif nums[i] == 2:
                    b -= 1
                    nums[b], nums[i] = nums[i], nums[b]
            i += 1
