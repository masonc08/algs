# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        L = 0
        run = head
        while run:
            L += 1
            run = run.next
        run = head
        for _ in range(L//2-1):
            run = run.next
        run.next = run.next.next
        return head
