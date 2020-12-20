"""
Leetcode 1695
Leetcode weekly contest 220
Runtime: 1328 ms, faster than 33.33% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.3 MB, less than 33.33% of Python3 online submissions for Maximum Erasure Value.
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sol = cur = nums[0]
        i, j, seen = 0, 1, set([nums[0]])
        while j < len(nums):
            cur += nums[j]
            if nums[j] in seen:
                while nums[i] != nums[j]:
                    cur -= nums[i]
                    seen.remove(nums[i])
                    i += 1
                cur -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            sol = max(sol, cur)
            j += 1
        return sol
