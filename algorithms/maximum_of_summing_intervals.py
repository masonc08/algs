"""
20:36
Given length of array
given set of intervals within the array: tuple of 3 numbers, first 2 is interval, third is number toadd between interval
return max value after all ops finished
(0, 2, 5)
(1, 3, 2)
(2, 4, 1)

[5,2,1,-5,-2,-1]
[5,7,8,3,1,0]
[5, 2, 5, 2, 0]
    7  7  2 

[[0], [1], [0, 2], [1], [2]]


 5  7  7  2  0

[(0, 2, 1), (1, 3, 2), (1, 2, 2), (3, 5, 3)]
"""


import itertools


class Solution:
    def solve(self, intervals, n):
        L = max(intervals, key=lambda x: x[1])
        li = [0]*(L+1)
        for s, e, v in intervals:
            li[s] += v
            li[e+1] -= v
        return max(itertools.accumulate(intervals))
