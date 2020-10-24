"""
https://leetcode.com/discuss/interview-question/241808/Google-Two-sum-closest
"""

class Solution:
    def twoSumClosest(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0
        j = len(nums)-1
        sol = [i, j, target-(nums[i]+nums[j])]
        while i != j:
            s = nums[i] + nums[j]
            if target-s < sol[2]:
                sol = [i, j, target-s]
            if s == target:
                break
            if s > target:
                j -= 1
            else:
                i += 1
        return sol[:2]