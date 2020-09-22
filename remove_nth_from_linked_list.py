# Leetcode 19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        self.n = n
        max_length, done = self._removeNthFromEnd(head, 0)
        if self.n == max_length and not done:
            head = head.next
        return head

    def _removeNthFromEnd(self, node, length):
        if node.next == None:
            return (length+1, False)
        max_length, done = self._removeNthFromEnd(node.next, length+1)
        if done:
            return (max_length, True)
        if max_length - self.n == length+1:
            node.next = node.next.next
            return (max_length, True)
        return (max_length, False)
