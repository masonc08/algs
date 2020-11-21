"""
Leetcode 902
November Leetcoding challenge
Runtime: 32 ms, faster than 55.10% of Python3 online submissions for Numbers At Most N Given Digit Set.
Memory Usage: 14.4 MB, less than 9.18% of Python3 online submissions for Numbers At Most N Given Digit Set.
"""


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        slimit = str(n)
        dp = [0]*len(slimit) + [1]
        for i in reversed(range(len(slimit))):
            v = int(slimit[i])
            for num in digits:
                num = int(num)
                if num < v:
                    dp[i] += len(digits)**(len(slimit)-i-1)
                elif num == v:
                    dp[i] += dp[i+1]
        base = 0
        for i in range(1, len(slimit)):
            base += len(digits)**i
        return base+dp[0]
