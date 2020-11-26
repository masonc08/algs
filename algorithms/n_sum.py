"""
Generalized algorithm for computing collections of n > 1 integers in an array that 
sum to a target value, inspired by
https://leetcode.com/problems/4sum/discuss/8609/My-solution-generalized-for-kSums-in-JAVA
Assumptions:
- No repeated elements
- At least one solution exists in given array
- n > 1
"""


from typing import List


class Solution:
    def nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        if n == 1:
            return [[target]]
        if n == 2:
            return self._twoSum(nums, target)
        if n >= 3:
            nums.sort()
            sol = []
            for i, num in enumerate(nums):
                sol += self._nSum(i+1, nums, target-num, n-1, [num])
            return sol


    def _nSum(self, start, nums, target, n, prefix):
        sol = []
        if n == 2:
            i, j = start, len(nums)-1
            while i < j:
                ttl = nums[i] + nums[j]
                if ttl > target:
                    j -= 1
                elif ttl < target:
                    i += 1
                else:
                    sol.append(prefix+[nums[i], nums[j]])
                    i += 1
                    j -= 1
            return sol
        else:
            for i in range(start, len(nums)):
                num = nums[i]
                prefix.append(num)
                sol += self._nSum(i+1, nums, target-num, n-1, prefix)
                prefix.pop()
            return sol


    def _twoSum(self, nums, target):
        seen = set()
        sol = []
        for num in nums:
            if target-num in seen:
                sol.append([num, target-num])
            seen.add(num)
        return sol

f = Solution().nSum
assert f([4, 2, 1, 5, 6, 2, 3], 8, 4) == [[1, 2, 2, 3]]
assert f([1, 0, 3, 2, 6, 5], 6, 2) == [[6, 0], [5, 1]]
