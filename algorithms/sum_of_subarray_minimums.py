"""
Leetcode 907
"""


class Solution:
    MOD = 10**9+7

    """
    O(n) runtime, O(n) space using stack to find min ranges for each number
    Runtime: 600 ms, faster than 12.46% of Python3 online submissions for Sum of Subarray Minimums.
    Memory Usage: 19 MB, less than 18.51% of Python3 online submissions for Sum of Subarray Minimums.
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l, r, s = [0]*len(arr), [0]*len(arr), []
        for i in range(len(arr)):
            ct = 1
            while s and s[-1][0] > arr[i]:
                ct += s.pop()[1]
            l[i] = ct
            s.append((arr[i], ct))
        s = []
        for i in range(len(arr)-1, -1, -1):
            ct = 1
            while s and s[-1][0] >= arr[i]:
                ct += s.pop()[1]
            r[i] = ct
            s.append((arr[i], ct))
        return sum(a*l*r for a, l, r in zip(arr, l, r)) % self.MOD


    """
    O(n^2) runtime, O(n) space by enumeration
    TLE
    """
    # def sumSubarrayMins(self, arr: List[int]) -> int:
    #     sol = 0
    #     while arr:
    #         tmp = [0]*(len(arr)-1)
    #         sol += arr[0]
    #         sol %= self.MOD
    #         if len(tmp) == 0:
    #             return sol
    #         for i in range(1, len(arr)):
    #             sol += arr[i]
    #             sol %= self.MOD
    #             tmp[i-1] = min(arr[i], arr[i-1])
    #         arr = tmp
    #     return sol
