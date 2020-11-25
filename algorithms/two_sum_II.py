"""
Leetcode 167
Runtime: 64 ms, faster than 47.48% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.5 MB, less than 12.90% of Python3 online submissions for Two Sum II - Input array is sorted.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            ttl = numbers[i]+numbers[j]
            if ttl > target:
                j -= 1
            elif ttl < target:
                i += 1
            else:
                return [i+1, j+1]
        raise Exception()
