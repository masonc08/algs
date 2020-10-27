"""
Leetcode 859
Runtime: 32 ms, faster than 69.61% of Python3 online submissions for Buddy Strings.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        exist = set()
        dupes = False
        a = None
        swapped = False
        i = 0
        while i < len(A):
            if A[i] in exist:
                dupes = True
            exist.add(A[i])
            if A[i] != B[i]:
                if swapped:
                    return False
                if a is None:
                    a = i
                    i += 1
                else:
                    if A[i] == B[a] and A[a] == B[i]:
                        swapped = True
                        i += 1
                    else:
                        return False
            else:
                i += 1
        if a is not None and not swapped:
            return False
        if a is None and dupes:
            return True
        return swapped
