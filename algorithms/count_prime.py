"""
Leetcode 204
Runtime: 484 ms, faster than 70.92% of Python3 online submissions for Count Primes.
Memory Usage: 25.4 MB, less than 5.09% of Python3 online submissions for Count Primes.
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        count = 0
        cache = [False]*n
        for i in range(2, n):
            if cache[i]:
                continue
            for j in range(i*i, n, i):
                cache[j] = True
            count += 1
        return count
