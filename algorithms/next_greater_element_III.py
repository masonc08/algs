"""
Leetcode 556
December Leetcoding challenge
Runtime: 28 ms, faster than 74.38% of Python3 online submissions for Next Greater Element III.
Memory Usage: 14.2 MB, less than 32.84% of Python3 online submissions for Next Greater Element III.
"""


import collections


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = [ [-1, 0] for _ in range(10)]
        n = list(str(n))
        for i in range(len(n)-1, -1, -1):
            num = int(n[i])
            if arr[num][0] == -1:
                arr[num][0] = i
            arr[num][1] += 1
            for j in range(num+1, 10):
                if arr[j][0] != -1:
                    other = arr[j][0]
                    n[i], n[other] = n[other], n[i]
                    arr[j][1] -= 1
                    i += 1
                    for k in range(10):
                        while arr[k][1]:
                            arr[k][1] -= 1
                            n[i] = str(k)
                            i += 1
                    sol = int(''.join(n))
                    if sol > 0x7fffffff:
                        return -1
                    return sol
        return -1
