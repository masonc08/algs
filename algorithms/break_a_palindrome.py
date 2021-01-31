"""
Leetcode 1328
O(n) runtime and space
Runtime: 32 ms, faster than 53.79% of Python3 online submissions for Break a Palindrome.
Memory Usage: 14.4 MB, less than 16.42% of Python3 online submissions for Break a Palindrome.
"""


class Solution:
    def breakPalindrome(self, S: str) -> str:
        L = len(S)
        if L == 1:
            return ''
        for i in range(L//2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i+1:]
        return S[:L-1] + 'b'
