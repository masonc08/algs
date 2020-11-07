"""
Leetcode 445
Novemeber Leetcoding challenge
Runtime: 64 ms, faster than 96.52% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sizes = sorted([(l1, self._get_length(l1)), (l2, self._get_length(l2))], key=lambda x: x[1])
        longrunner, shortrunner = sizes[-1][0], sizes[0][0]
        longcounter, shortcounter = sizes[-1][1], sizes[0][1]
        n = 0
        while longcounter != 0 and shortcounter != 0:
            n *= 10
            cur = longrunner.val
            if longcounter == shortcounter:
                cur += shortrunner.val
                shortcounter -= 1
                shortrunner = shortrunner.next
            longrunner = longrunner.next
            longcounter -= 1
            n += cur
        prev = None
        if n == 0:
            return ListNode(0)
        while n:
            prev = ListNode(n%10, prev)
            n //= 10
        return prev


    def _get_length(self, li: ListNode) -> int:
        sol = 0
        run = li
        while run:
            sol += 1
            run = run.next
        return sol
