"""
Leetcode 1712
Leetcode weekly contest 222
Runtime: 6824 ms, faster than 100.00% of Python3 online submissions for Ways to Split Array Into Three Subarrays.
Memory Usage: 27.4 MB, less than 100.00% of Python3 online submissions for Ways to Split Array Into Three Subarrays.
"""


class Solution:
    MOD = 10**9+7
    def waysToSplit(self, nums: List[int]) -> int:
        L = len(nums)
        for i in range(1, L):
            nums[i] += nums[i-1]
        sol = 0
        for i in range(1, L-1):
            l, r = self.left_search(nums[i-1], i, nums), self.right_search(nums[i-1], i, nums)
            if l == -1 or r == -1:
                continue
            sol += (r-l+1)%self.MOD
            sol %= self.MOD
        return sol

    left_search = lambda self, lsum, l, nums: self.search(lsum, l, nums)
    right_search = lambda self, lsum, l, nums: self.search(lsum, l, nums, left=False)

    def search(self, lsum, l, nums, left=True):
        L = len(nums)
        r = L-2
        sol = -1
        while l <= r:
            m = (l+r+1)//2
            msum, rsum = nums[m]-lsum, nums[L-1]-nums[m]
            if lsum <= msum <= rsum:
                sol = m
                if left:
                    r = m-1
                else:
                    l = m+1
            elif lsum > msum:
                l = m+1
            else:
                r = m-1
        return sol
