"""
Leetcode 148
Runtime: 716 ms, faster than 5.04% of Python3 online submissions for Sort List.
Memory Usage: 29.9 MB, less than 6.25% of Python3 online submissions for Sort List.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        du = ListNode(next=head)
        length = self._get_length(head)
        if length < 2:
            return head
        size = 1
        while size <= length:
            size *= 2
            main = du
            while main.next:
                mid, end = self._get_mid_and_end(main.next, size)
                main.next, main = self._merge(main.next, mid, end)
        return du.next


    def _get_mid_and_end(self, start, nnodes):
        run, count, mid = start, 0, None
        while run and count < nnodes:
            if count == nnodes//2:
                mid = run
            count += 1
            run = run.next
        return mid, run


    def _merge(self, start, mid, end):
        head = runner = ListNode()
        lrun, rrun = start, mid
        while lrun is not mid or rrun is not end:
            if lrun is mid or (rrun is not end and lrun.val >= rrun.val):
                if lrun is None:
                    return head.next, runner
                runner.next, runner, rrun = rrun, rrun, rrun.next
            else:
                runner.next, runner, lrun = lrun, lrun, lrun.next
        runner.next = end
        return head.next, runner


    def _get_length(self, head):
        sol = 0
        while head:
            sol += 1
            head = head.next
        return sol
