"""
Twitch OA 2020, missing dice rolls
https://leetcode.com/discuss/interview-question/700704/Amazon-or-OA-2020-or-Missing-Dice-Rolls

You have just rolled a dice several times. The N roll results that you remember are described by an array A. However, there are F rolls whose results you have forgotten. The arithmetic mean of all of the roll results (the sum of all the roll results divided by the number of rolls) equals M.
What are the possible results of the missing rolls?

Write a function:
vector<int> solution(vector<int> &A, int F, int M):

that, given an array A of length N, an integer F and an integer M, returns an array containing the possible results of the missed rolls. The returned integers should contain M integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return [0].

Examples:

Given A = [3, 2, 4, 3], F = 2, M = 4, your function should return [6, 6].
Given A= [1, 5, 6], F = 4, M = 3, your function may return [2, 1, 2, 4] or [6, 1, 1, 1] among others.
Given A = [1, 2, 3, 4], F = 4, M = 6, your function should return [0]. It is not possible to obtain such a mean.
"""

class Solution:
    def missingDiceRolls(self, A, F, M):
        ttl = M*(F+len(A))
        sol = [1]*F
        ttl -= sum(A)
        ttl -= F
        for i in range(len(sol)):
            if ttl >= 5:
                sol[i] += 5
                ttl -= 5
            elif ttl > 0:
                sol[i] += ttl
                ttl = 0
            else:
                return [0]
        return sol if ttl == 0 else [0]
