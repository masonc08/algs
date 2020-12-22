"""
Leetcode 930
Runtime: 296 ms, faster than 18.86% of Python3 online submissions for Binary Subarrays With Sum.
Memory Usage: 14.8 MB, less than 94.28% of Python3 online submissions for Binary Subarrays With Sum.
"""


class Solution:
    """
    Sliding window
    """
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def solve(S):
            if S<0:
                return 0
            sol = i = 0
            for j, v in enumerate(A):
                S -= v
                while S < 0:
                    S += A[i]
                    i += 1
                sol += (j-i+1)
            return sol
        return solve(S)-solve(S-1)
    
    # Sliding window with left interval
    # def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    #     i = i1 = sol = cur = 0
    #     for j, n in enumerate(A):
    #         cur += n
    #         while i < j and cur > S:
    #             cur -= A[i]
    #             i += 1
    #         i1 = i
    #         while i1 < j and A[i1] == 0:
    #             i1 += 1
    #         if cur == S:
    #             sol += (i1-i+1)
    #     return sol

# Prefix sum solution
# class Solution:
#     def numSubarraysWithSum(self, A: List[int], S: int) -> int:
#         mp = collections.Counter()
#         mp[0] = 1
#         cur = 0
#         sol = 0
#         for n in A:
#             cur += n
#             if cur-S in mp:
#                 sol += mp[cur-S]
#             mp[cur] += 1
#         return sol