"""
Leetcode 443
Runtime: 48 ms, faster than 97.37% of Python3 online submissions for String Compression.
Memory Usage: 14.3 MB, less than 50.46% of Python3 online submissions for String Compression.
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        l = 1
        L = len(chars)
        for j in range(1, L+1):
            if j < L and chars[j] == chars[j-1]:
                l += 1
            if j == L or chars[j] != chars[j-1]:
                if l == 1:
                    chars[i] = chars[j-1]
                    i += 1
                else:
                    tmp = str(l)
                    chars[i:i+len(tmp)+1] = (chars[j-1],) + tuple(tmp)
                    i += len(tmp)+1
                l = 1
        return i
