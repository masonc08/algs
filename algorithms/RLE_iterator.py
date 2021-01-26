"""
Leetcode 900
O(n) worst-case runtime per query, O(1) runtime constructor, O(1) space overall
Runtime: 36 ms, faster than 80.86% of Python3 online submissions for RLE Iterator.
Memory Usage: 14.8 MB, less than 86.21% of Python3 online submissions for RLE Iterator.
"""


class RLEIterator:

    def __init__(self, A: List[int]):
        self.A, self.L, self.i = A, len(A), 0

    def next(self, n: int) -> int:
        while n:
            while self.i == self.L or self.A[self.i] == 0:
                if self.i == self.L:
                    return -1
                self.i += 2
            x = min(n, self.A[self.i])
            n -= x
            self.A[self.i] -= x
        return self.A[self.i+1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)