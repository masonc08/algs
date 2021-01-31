"""
Leetcode 1744
Leetcode weekly contest 226
O(M+N) runtime, O(M) space, where M=len(queries), N=len(candiesCount)
Runtime: 1544 ms, faster than 66.67% of Python3 online submissions for Can You Eat Your Favorite Candy on Your Favorite Day?.
Memory Usage: 73.1 MB, less than 55.56% of Python3 online submissions for Can You Eat Your Favorite Candy on Your Favorite Day?.
"""


import itertools


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        A = tuple(itertools.accumulate(candiesCount, initial=0))
        return [fday < A[ftype+1] and (fday+1)*cap-1 >= A[ftype] for ftype, fday, cap in queries]