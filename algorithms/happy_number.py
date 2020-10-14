# Leetcode 202


class Solution:
    def isHappy(self, n):
        x = n
        y = n
        while 1:
            x = Solution._next_num(x)
            if x == 1:
                return True
            y = Solution._next_num(Solution._next_num(y))
            if y == 1:
                return True
            if x == y:
                return False

    @staticmethod
    def _next_num(n):
        sum_of_sqs = 0
        while n != 0:
            sum_of_sqs += (n % 10) * (n % 10)
            n //= 10
        return sum_of_sqs

