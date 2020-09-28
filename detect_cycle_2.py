# Leetcode 142

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        if fast is None or fast.next is None:
            return None
        slow2 = head
        while not(slow2 is slow):
            slow2 = slow2.next
            slow = slow.next
        return slow