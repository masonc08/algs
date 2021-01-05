"""
Leetcode 946
Runtime: 64 ms, faster than 93.85% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.6 MB, less than 23.08% of Python3 online submissions for Validate Stack Sequences.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        L = len(popped)
        j = 0
        for v in pushed:
            stk += v,
            while stk and j < L and popped[j] == stk[-1]:
                stk.pop()
                j += 1
        return len(stk) == 0
