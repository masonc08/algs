"""
Leetcode 263
Runtime: 32 ms, faster than 58.39% of Python3 online submissions for Ugly Number.
Memory Usage: 14.2 MB, less than 23.01% of Python3 online submissions for Ugly Number.
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        num = abs(num)
        poss = [False]*num
        for i in range(2, num+1):
            if not poss[i-1]:
                j = i+i
                while j <= num-1:
                    poss[j-1] = True
                    j += i
                if num%i == 0 and i not in {2, 3, 5}:
                    return False
        return True
