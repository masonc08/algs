"""
Leetcode 673
O(NN) runtime, O(N) space
DP
Runtime: 1188 ms, faster than 80.85% of Python3 online submissions for Number of Longest Increasing Subsequence.
Memory Usage: 14.6 MB, less than 51.58% of Python3 online submissions for Number of Longest Increasing Subsequence.
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        sizes, occs = [1]*L, [1]*L
        mlen = sol = 0
        for i, v in enumerate(nums):
            for j in range(i):
                if nums[j] < v:
                    if sizes[j]+1 > sizes[i]:
                        sizes[i], occs[i] = sizes[j]+1, occs[j]
                    elif sizes[j]+1 == sizes[i]:
                        occs[i] += occs[j]
            if mlen == sizes[i]:
                sol += occs[i]
            elif mlen < sizes[i]:
                mlen, sol = sizes[i], occs[i]
        return sol
