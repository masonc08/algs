"""
Leetcode 86
Runtime: 72 ms, faster than 8.89% of Python3 online submissions for Partition List.
Memory Usage: 14.4 MB, less than 7.24% of Python3 online submissions for Partition List.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        low, high = ListNode(), ListNode()
        lrun = low
        hrun = high
        run = head
        while run:
            if run.val < x:
                lrun.next = run
                lrun = lrun.next
            else:
                hrun.next = run
                hrun = hrun.next
            run = run.next
        hrun.next = None
        lrun.next = high.next
        return low.next
