"""
Leetcode 1414
Runtime: 36 ms, faster than 64.37% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
Memory Usage: 14.3 MB, less than 40.80% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] + fib[-2] <= k:
            fib += (fib[-1]+fib[-2]),
        L = len(fib)
        r = L-1
        k -= fib[r]
        sol = 1
        while k:
            r -= 1
            l = 0
            while l < r:
                m = (l+r+1)//2
                if fib[m] < k:
                    l = m
                elif fib[m] > k:
                    r = m-1
                else:
                    l = r = m
            k -= fib[l]
            sol += 1
        return sol
