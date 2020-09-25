# Leetcode 24

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        runner = head
        head = runner.next
        temp = runner.next.next
        runner.next.next = runner
        runner.next = temp
        while runner and runner.next and runner.next.next:
            temp = runner.next.next
            runner.next.next = runner.next.next.next
            temp.next = runner.next
            runner.next = temp
            runner = runner.next.next
        return head