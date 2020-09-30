# Leetcode 82
# 78.87% Time, 5.40% Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.next = head
        del_mode = False
        slow = self
        fast = self.next
        while fast:
            if fast.next and fast.val == fast.next.val:
                del_mode = True
            else:
                if del_mode:
                    slow.next = fast.next
                    del_mode = False
                else:
                    slow = slow.next
            fast = fast.next
        return self.next
