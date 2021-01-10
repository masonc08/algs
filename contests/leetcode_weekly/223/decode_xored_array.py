"""
Leetcode 1720
Leetcode weekly contest 223
O(n) runtime and space
Runtime: 296 ms, faster than 100.00% of Python3 online submissions for Decode XORed Array.
Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Decode XORed Array.
"""


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        sol = [0]*(len(encoded)+1)
        sol[0] = first
        for i in range(len(sol)-1):
            sol[i+1] = sol[i]^encoded[i]
        return sol
