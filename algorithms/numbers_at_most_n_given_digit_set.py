"""
Leetcode 902
November Leetcoding challenge
Runtime: 32 ms, faster than 55.10% of Python3 online submissions for Numbers At Most N Given Digit Set.
Memory Usage: 14.4 MB, less than 9.18% of Python3 online submissions for Numbers At Most N Given Digit Set.
"""


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits.sort()
        slimit = str(n)
        prev, cur = 1, 0
        for i in reversed(range(len(slimit))):
            v = int(slimit[i])
            for num in digits:
                num = int(num)
                if num < v:
                    cur += len(digits)**(len(slimit)-i-1)
                elif num == v:
                    cur += prev
                    break
            cur, prev = 0, cur
        base = 0
        for i in range(1, len(slimit)):
            base += len(digits)**i
        return base+prev
