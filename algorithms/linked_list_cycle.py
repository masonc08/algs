# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        turtle = rabbit = head
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
            if turtle is rabbit:
                return True
        return False
