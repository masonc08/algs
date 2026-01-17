from typing import List

class Solution:
    MOD = 10**9+7
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        cache = {}
        def _recursive(i, target1, target2, cur):
            if (i, target1, cur) in cache:
                return cache[i, target1, cur]
            if i == len(nums):
                return 1 if cur == target1 else 0
            count = 0
            if cur == target1:
                count += _recursive(i+1, target2, target1, nums[i]) % self.MOD
            count += _recursive(i+1, target1, target2, cur^nums[i]) % self.MOD
            cache[i, target1, cur] = count % self.MOD
            return count % self.MOD
        return _recursive(1, target1, target2, nums[0])


# from typing import List
# import itertools, functools

# class Solution:
#     def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
#         xor_cache = {}
#         @functools.lru_cache(10000)
#         def _recursive(i, target1, target2):
#             if i == len(nums):
#                 return 1
#             valid_partitions = 0
#             prev_xor = 0
#             for j in range (i, len(nums)):
#                 xor_result = prev_xor ^ nums[j]
#                 if xor_result == target1:
#                     valid_partitions += _recursive(j+1, target2, target1)
#                 prev_xor = xor_result
#             return valid_partitions%1000000007
        
#         return _recursive(0, target1, target2)