"""
Leetcode 141
Runtime: 48 ms, faster than 66.51% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.1 MB, less than 67.60% of Python3 online submissions for Linked List Cycle.
"""


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
