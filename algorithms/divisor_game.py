"""
Leetcode 1025
Runtime: 28 ms, faster than 81.60% of Python3 online submissions for Divisor Game.
Memory Usage: 14.1 MB, less than 87.24% of Python3 online submissions for Divisor Game.
"""


class Solution:
    """
    O(1) runtime and space
    Mathematical Solution
    [14:18] Mason: odd numbers have ONLY odd factors, so if you pick any of those odd factors, let's say A, and do you N-A, you're going to do odd-odd, which results in an even number
    [14:18] Mason: that even number is passed to the other person
    [14:19] Mason: meaning that if you start with an odd number, you ALWAYS pass an even number to the other person
    [14:19] Mason: if you start with an even number, you can choose to pass an odd or even number to the other person since even numbers have odd and even factors
    [14:20] Mason: but if we look at the case where n <= 3, if alice has 3 and subtracts 1(only choice), bob get 2
    [14:20] Mason: then bob does the same, alice gets 1
    [14:20] Mason: and alice loses
    [14:20] Mason: which means that if you have an odd number you always lose, you dont want to have an odd number
    [14:20] Mason: so combined with what I said in the first part it should mean that if alice starts with an odd number she losess
    """
    # def divisorGame(self, n: int) -> bool:
    #     return N%2 == 0

    """
    O(n^(3/2)) runtime, O(n) space
    DP Solution
    """
    def divisorGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(n+1):
            factors = self.get_factors(i)
            dp[i] = any(not dp[i-factor] for factor in factors if factor < i)
        return dp[n]

    def get_factors(self, n):
        sol = []
        i = 1
        while i*i <= n:
            if n%i == 0:
                sol += i,
                if i*i != n:
                    sol += n//i,
            i += 1
        return sol
