"""
Leetcode 125
Runtime: 48 ms, faster than 60.19% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.7 MB, less than 40.62% of Python3 online submissions for Valid Palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isnumeric()):
                i += 1
            while i < j and not (s[j].isalpha() or s[j].isnumeric()):
                j -= 1
            if i >= j:
                return True
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
