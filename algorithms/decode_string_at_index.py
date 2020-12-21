"""
Leetcode 880
December Leetcoding challenge
Runtime: 32 ms, faster than 44.72% of Python3 online submissions for Decoded String at Index.
Memory Usage: 14.4 MB, less than 6.50% of Python3 online submissions for Decoded String at Index.
"""


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        cur = 0
        while 1:
            for c in S:
                if not c.isnumeric():
                    cur += 1
                    if cur == K:
                        return c
                else:
                    c = int(c)
                    if cur*c < K:
                        cur *= c
                    else:
                        K -= cur
                        cur = 0
                        break
