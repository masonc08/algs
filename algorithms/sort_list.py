"""
Leetcode 148
Runtime: 716 ms, faster than 5.04% of Python3 online submissions for Sort List.
Memory Usage: 29.9 MB, less than 6.25% of Python3 online submissions for Sort List.
"""
# TODO: Bad solution, consider revising

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        self.next = head
        length = self._get_length(head)
        if length < 2:
            return head
        size = 1
        while size <= length:
            size *= 2
            main = self
            while main.next:
                run = main.next
                count = 0
                mid = None
                while run and count < size:
                    if count == size//2:
                        mid = run
                    count += 1
                    run = run.next
                main.next, main = self._merge(main.next, mid, run)
        return self.next


    def _merge(self, start, mid, end):
        head = runner = ListNode()
        lrun = start
        rrun = mid
        while lrun is not mid or rrun is not end:
            if lrun is mid:
                if lrun is None:
                    return head.next, runner
                runner.next = rrun
                runner = runner.next
                rrun = rrun.next
            elif rrun is end:
                runner.next = lrun
                runner = runner.next
                lrun = lrun.next
            elif lrun.val < rrun.val:
                runner.next = lrun
                runner = runner.next
                lrun = lrun.next
            elif lrun.val >= rrun.val:
                runner.next = rrun
                runner = runner.next
                rrun = rrun.next
            runner.next = end
        return head.next, runner


    def _get_length(self, head):
        i = head
        sol = 0
        while i:
            sol += 1
            i = i.next
        return sol
