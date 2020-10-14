#  Leetcode 143

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stk = []
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        while slow:
            stk.append(slow)
            slow = slow.next
        slow = head
        while stk:
            last = stk.pop()
            if last is slow:
                slow.next = None
                return
            if last is slow.next:
                slow.next.next = None
                return
            slow.next, last.next = last, slow.next
            slow = slow.next.next
