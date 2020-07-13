# Leetcode 70

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        last_two = [0]*2
        last_two[0], last_two[1] = 1, 1
        for i in range(2, n):
            last_two[0], last_two[1] = last_two[1], last_two[0]
            temp = sum(last_two)
            last_two[1] = temp
        return sum(last_two)


print(Solution().climbStairs(7))
