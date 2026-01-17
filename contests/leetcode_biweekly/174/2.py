class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        unique = set()
        for a, b in zip(nums, target):
            if a == b:
                continue
            unique.add(a)
        return len(unique)
    