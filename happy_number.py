# Leetcode 202


class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            sum_of_sqs = 0
            seen.add(n)
            while n != 0:
                sum_of_sqs += (n % 10) * (n % 10)
                n //= 10
            n = sum_of_sqs
        return n == 1


print(Solution().isHappy(19))
