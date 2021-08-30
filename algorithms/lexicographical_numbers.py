"""
Leetcode 386
July Leetcoding challenge
"""


from typing import List
import collections, bisect, heapq, itertools, functools, math


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        digits = math.floor(math.log10(n))+1 
        sol, i = [0]*n, 1
        for j in range(digits):
            sol[i] = 10**j
            i += 1
        for j in range(digits-1, 0, -1):
            quantity = 10**j-1 if 10**j < n else n-10**j
            sol[i:(i:=i+quantity)] = range(10**j, 10**j if 10**j < n else n+1)

